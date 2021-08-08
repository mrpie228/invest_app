from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import logging
from celery.schedules import crontab

logger = logging.getLogger("Celery")
print('===================')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('cel_task')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'parse-stock': {
        'task': 'cel_task.tasks.show_hello_world',
        'schedule': crontab(minute='*/60'),
    }
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
