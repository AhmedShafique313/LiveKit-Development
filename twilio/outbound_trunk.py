import asyncio

from livekit import api
from livekit.protocol.sip import CreateSIPOutboundTrunkRequest, SIPOutboundTrunkInfo

async def main():
  lkapi = api.LiveKitAPI()

  trunk = SIPOutboundTrunkInfo(
    name = "demo trunk",
    address = "kavtechdemo.pstn.twilio.com",
    numbers = ['+12513134900'],
    auth_username = "kavtech_cred_313",
    auth_password = "@Kavtech313Ahmed"
  )

  request = CreateSIPOutboundTrunkRequest(
    trunk = trunk
  )

  trunk = await lkapi.sip.create_sip_outbound_trunk(request)

  print(f"Successfully created {trunk}")

  await lkapi.aclose()

asyncio.run(main())