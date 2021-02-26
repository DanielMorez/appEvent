from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'appEvent.settings')

app = Celery('appEvent')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# celery beat tasks

app.conf.beat_schedule = {
    'check-news-every-5-minute': {
        'task': 'mainapp.tasks.beat_update_news',
        'schedule': crontab(minute='*/5')
    }
}