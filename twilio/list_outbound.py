import asyncio

from livekit import api
from livekit.protocol.sip import ListSIPOutboundTrunkRequest

async def main():
  livekit_api = api.LiveKitAPI()

  rules = await livekit_api.sip.list_sip_outbound_trunk(
    ListSIPOutboundTrunkRequest()
  )
  print(f"{rules}")

  await livekit_api.aclose()

asyncio.run(main())