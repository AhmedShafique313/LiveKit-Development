import asyncio
from dotenv import load_dotenv
from livekit import api 
from livekit.protocol.sip import CreateSIPParticipantRequest, SIPParticipantInfo
import os

load_dotenv(dotenv_path=".env")
async def main():
    # livekit_api = api.LiveKitAPI(
    #     url=os.getenv("LIVEKIT_URL"),
    #     api_key=os.getenv("LIVEKIT_API_KEY"),
    #     api_secret=os.getenv("LIVEKIT_API_SECRET")
    # )

    livekit_api = api.LiveKitAPI(
    url="wss://test1-z93avhzw.livekit.cloud",
    api_key="APIYWv5YKLExkVg",      
    api_secret="U6q00U4sTTfVcchXEuBSp4dX8gUhRnQgG0mduvtEGSW" 
    )

    request = CreateSIPParticipantRequest(
        sip_trunk_id = "ST_d5BBmUtkvhRa",
        sip_call_to = "+923300349075",
        room_name = "open-room",
        participant_identity = "sip-test",
        participant_name = "Test call participant",
        krisp_enabled = True,
        wait_until_answered = True
    )
    
    try:
        participant = await livekit_api.sip.create_sip_participant(request)
        print(f"Successfully created {participant}")
    except Exception as e:
        print(f"Error creating SIP participant: {e}")
    finally:
        await livekit_api.aclose()

asyncio.run(main())