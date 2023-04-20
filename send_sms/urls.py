from .views import send_sms_view,sms_view,sms_view1
from django.urls import path
urlpatterns = [
    # other URL patterns
    path('send-sms/', send_sms_view, name='send_sms'),
    path('sms/', sms_view, name='sms'),
    path('send/',sms_view1,name='django_sms'),                    

]
