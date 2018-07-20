
from twilio.rest import Client
import sys


def send_message():

    account_sid = "ACb06382cd4aa268ef0c8011cfea48224c"
    auth_token  = "141faaf93bcc278ec3d9789ccddf4b17"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=sys.argv[2],
        from_="(613) 900-5909",
        body=sys.argv[1])

    print(message.sid)


send_message()
