from twilio.rest import Client
import os
# Your Account SID and Auth Token from console.twilio.com
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

# message = client.messages.create(
#     to="+923300349075",
#     from_="+12513134900",
#     body="Hello, this is Ahmed")
call = client.calls.create(
    twiml="<Response><Say>Ahoy, World!</Say></Response>",
    to="+923300349075",
    from_="+12513134900",
)

# print(message.sid)
print(call.sid)