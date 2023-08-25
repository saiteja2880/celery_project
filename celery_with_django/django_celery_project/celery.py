from __future__ import absolute_import,unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_celery_project.settings')

app = Celery('django_celery_project')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace = 'CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    'print_hello_every_minute':{
        'task' : 'mainapp.tasks.print_hello',
        'schedule': crontab(minute='*/1')
    }
}

app.conf.beat_schedule = {
    'print_hii_every_10sec':{
        'task':'mainapp.tasks.hii',
        'schedule' : crontab(minute = '*/1')
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
