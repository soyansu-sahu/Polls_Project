
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'polls.settings')
celery_app = Celery('polls')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'send-poll-notification': {
        'task': 'polls_app.task.send_poll_notification',
        'schedule': crontab(minute=13, hour=22),
    },
}
