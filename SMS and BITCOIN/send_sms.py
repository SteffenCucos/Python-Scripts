from twilio.rest import Client

def send_message(message,dest):

    account_sid = "ACb06382cd4aa268ef0c8011cfea48224c"
    auth_token  = "141faaf93bcc278ec3d9789ccddf4b17"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=dest,
        #to="+16474479131",
        from_="(613) 900-5909",
        body=message)

    print(message.sid)



