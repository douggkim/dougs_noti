from twilio.rest import Client
import os 


def send_text(account_sid, auth_token, from_number, to_number, text_body): 
    account_sid = account_sid
    auth_token = auth_token
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_=from_number,
    body=text_body,
    to=to_number
    )

    print(message.sid)


to_number = '+14244686697'
from_number = '+18449991359'
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

send_text(account_sid=account_sid, auth_token=auth_token, from_number=from_number, to_number=to_number, text_body="Sending test #3")