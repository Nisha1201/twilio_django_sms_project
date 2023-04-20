from django.shortcuts import render, HttpResponse
from .tasks import send_sms_phone
from twilio.rest import Client
from django.views import View
from django.http import HttpResponse
from sms import send_sms
def send_sms_view(request):
    if request.method == "POST":
        to = request.POST['to']
        print(to,"ooooooooooooooooooooo")
        body = request.POST['body']
        print(body,"bbbbbbbbbbbbbbbbbbbbbb")
        send_sms_phone.delay(to, body)
    #     account_sid = 'AC9124c9f9d6ebad6bffa281e0d3604bb4'
    #     auth_token = '5ea5854a625244822d9b051e2547e15e'
    #     from_number = '+16073604837'
    #     client = Client(account_sid, auth_token)
    #     message = client.messages.create(
    #     from_=from_number,
    #     body="hello nisha sahu",
    #     to='+918563961069'
    #    )
        # print(message.sid)
        return HttpResponse('SMS sent')
    return render(request, 'send_sms.html')

def sms_view(request):
    account_sid = 'AC9124c9f9d6ebad6bffa281e0d3604bb4'
    auth_token = '5ea5854a625244822d9b051e2547e15e'
    from_number = '+16073604837'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=from_number,
        body="hello nisha sahu",
        to='+918563961069'
    )
    print(message.sid)


# django sms :

def sms_view1(request):
    send_sms(
        'Here is the message',
        '+16073604837',
        ['+918563961069'],
        fail_silently=False
    )
    print(send_sms)