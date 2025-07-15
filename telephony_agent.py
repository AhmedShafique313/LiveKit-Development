from dotenv import load_dotenv
import asyncio, logging, os, json, random
from livekit import api
from livekit import agents
from typing import Any
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    openai,
    cartesia,
    deepgram,
    noise_cancellation,
    silero,
    groq
)
from livekit.plugins.turn_detector.multilingual import MultilingualModel

# load_dotenv(dotenv_path=".env")
# outbound_trunk_id = os.getenv("SIP_OUTBOUND_TRUNK_ID")


class OutboundCaller(Agent):
    def __init__(self):
        super().__init__(
            instructions="You are a real estate digital assistant and you're talking on behalf of Ylopo. Your task is to help the user in terms of buying or selling a home."
        )


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt=deepgram.STT(),
        llm=groq.LLM(model="llama3-8b-8192"),
        tts=cartesia.TTS(),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

    await session.start(
        room=ctx.room,
        agent=OutboundCaller(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await ctx.connect()

    # Get phone number from dispatch metadata
    dial_info = json.loads(ctx.metadata) if ctx.metadata else {"phone_number": None}
    phone_number = dial_info.get("phone_number")

    sip_participant_identity = phone_number
    if phone_number is not None:
        try:
            await ctx.api.sip.create_sip_participant(api.CreateSIPParticipantRequest(
                room_name=ctx.room.name,
                sip_trunk_id="ST_YhYu2bronxxk",
                sip_call_to=phone_number,
                participant_identity=sip_participant_identity,
                wait_until_answered=True,
            ))

            print("Call picked up successfully")
        except api.TwirpError as e:
            print(f"Error creating SIP participant: {e.message}, "
                  f"SIP status: {e.metadata.get('sip_status_code')} "
                  f"{e.metadata.get('sip_status')}")
            ctx.shutdown()

    else:
        await session.generate_reply(
            instructions="Greet the user and offer your assistance."
        )

    
    await api.CreateAgentDispatchRequest(
        # Use the agent name you set in the WorkerOptions
        agent_name="my-telephony-agent", 

        # The room name to use. This should be unique for each call
        room=f"outbound-{''.join(str(random.randint(0, 9)) for _ in range(10))}",

        # Here we use JSON to pass the phone number, and could add more information if needed.
        metadata='{"phone_number": "+923300349075"}'
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(
        entrypoint_fnc=entrypoint,
        agent_name="my-telephony-agent"
    ))
