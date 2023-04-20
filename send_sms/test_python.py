# Download the helper library from https://www.twilio.com/docs/python/install
# import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid =  'AC9124c9f9d6ebad6bffa281e0d3604bb4'
auth_token = '5ea5854a625244822d9b051e2547e15e'
# phone_number='+18563961069'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there',
                              from_='+16073604837',
                              to='+18563961069',
                          )

print(message.sid)
print('send successfully')
