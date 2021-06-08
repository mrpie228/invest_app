from __future__ import absolute_import, unicode_literals
import logging

from django.conf import settings
from django_system.celery import app
from celery import shared_task

logger = logging.getLogger("celery")


# @app.on_after_finalize.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(
#         crontab(minute='*/1'),
#         parse_crypto.s()
#     )


@shared_task(name="parse_crypto")
def parse_crypto():
    print('F')


@app.task
def show_hello_world():
    logger.info("-" * 25)
    logger.info("Printing Hello from Celery")
    logger.info("-" * 25)
