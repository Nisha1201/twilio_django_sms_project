from celery import shared_task
from twilio.rest import Client

@shared_task
def send_sms_phone(to, body):
    # Your Twilio account sid and auth token
    account_sid = 'AC9124c9f9d6ebad6bffa281e0d3604bb4'
    auth_token = '5ea5854a625244822d9b051e2547e15e'
    from_number = '+16073604837'
    # Create a Twilio client
    client = Client(account_sid, auth_token)
    # Send the SMS
    message = client.messages.create(
        from_=from_number, 
        to=to,
        body=body,
    )
    return message.sid
