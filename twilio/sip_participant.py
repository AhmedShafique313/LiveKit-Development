import asyncio

from livekit import api 
from livekit.protocol.sip import CreateSIPParticipantRequest, SIPParticipantInfo

async def main():
    livekit_api = api.LiveKitAPI()

    request = CreateSIPParticipantRequest(
        sip_trunk_id = "ST_YhYu2bronxxk",
        sip_call_to = "+923300349075",
        room_name = "open-room",
        participant_identity = "sip-test",
        participant_name = "Test call participant",
        dtmf="*123#ww456",
        play_dialtone=True,
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