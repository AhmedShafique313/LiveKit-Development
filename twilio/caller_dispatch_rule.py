import asyncio
from livekit import api

async def main():
    lkapi = api.LiveKitAPI()
    
    request = api.CreateSIPDispatchRuleRequest(
        rule=api.SIPDispatchRule(
            dispatch_rule_individual=api.SIPDispatchRuleIndividual(
                room_prefix="call-",
            )
        ),
        room_config=api.RoomConfiguration(
            agents=[api.RoomAgentDispatch(
                agent_name="inbound-agent",
                metadata="job dispatch metadata",
            )]
        )
    )
    
    dispatch = await lkapi.sip.create_sip_dispatch_rule(request)
    print("created dispatch", dispatch)
    await lkapi.aclose()

# Run the async function
asyncio.run(main())