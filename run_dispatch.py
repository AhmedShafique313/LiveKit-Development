import asyncio
import random
import json
from livekit import api

async def dispatch_call():
    # Phone number to call
    phone_number = "+923300349075"

    # Create unique room name
    room_name = f"outbound-{''.join(str(random.randint(0, 9)) for _ in range(10))}"

    # Dispatch agent
    await api.agent_dispatch.create_dispatch(
        api.CreateAgentDispatchRequest(
            agent_name="my-telephony-agent",
            room=room_name,
            metadata=json.dumps({"phone_number": phone_number})
        )
    )

    print(f"Dispatched call to {phone_number} in room: {room_name}")


if __name__ == "__main__":
    asyncio.run(dispatch_call())
