from dotenv import load_dotenv
import asyncio, os
from livekit import api, agents
from livekit.agents import Agent, AgentSession, RoomInputOptions
from livekit.plugins import groq, cartesia, deepgram, silero, noise_cancellation
from livekit.plugins.turn_detector.multilingual import MultilingualModel

load_dotenv(dotenv_path=".env")
outbound_trunk_id = os.getenv("SIP_OUTBOUND_TRUNK_ID")

class OutboundCaller(Agent):
    def __init__(self):
        super().__init__(instructions="You are a helpful voice assistant")


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
    dial_info = {"phone_number": "+16467980578"}
    # dial_info = {"phone_number": "+923300349075"}
    phone_number = dial_info["phone_number"]

    sip_participant_identity = phone_number
    if phone_number is not None:
        try:
            await ctx.api.sip.create_sip_participant(api.CreateSIPParticipantRequest(
                room_name=ctx.room.name,
                sip_trunk_id=outbound_trunk_id,
                sip_call_to=phone_number,
                participant_identity=sip_participant_identity,
                wait_until_answered=True,
            ))
        
            print("call picked up successfully")
        except api.TwirpError as e:
            print(f"error creating SIP participant: {e.message}, "
                  f"SIP status: {e.metadata.get('sip_status_code')} "
                  f"{e.metadata.get('sip_status')}")
            ctx.shutdown()

    if phone_number is None:
        await session.generate_reply(
            instructions="Greet the user and offer your assistance."
        ) 

    # await session.generate_reply(
    #     instructions="Greet the user and offer your assistance."
    # )



if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(
        entrypoint_fnc=entrypoint,
        agent_name="my-outbound-agent"
    ))