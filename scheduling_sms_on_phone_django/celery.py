from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
# from datetime import timedelta

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scheduling_sms_on_phone_django.settings')
app = Celery('scheduling_sms_on_phone_django')
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
'Send_mail_to_Client': {
'task': 'send_sms.tasks.send_sms_phone',
'schedule': crontab(minute='*/1'),
'args': ('+918563961069',"hello Nisha Sahu................")
},

}

# 'schedule': 300.0, #every 30 seconds it will be called
# 'schedule': timedelta(minutes=2),


app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
 print(f'Request: {self.request!r}')