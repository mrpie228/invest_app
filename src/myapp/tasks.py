from __future__ import absolute_import, unicode_literals
import logging
from .celery import app
import os

logger = logging.getLogger("celery")


@app.task
def parse_crypto():
    # os.system('mkdir -m 777')
    # os.system('python3')
    # os.system(r'cd c_sharp_scripts/CryptoParse/exe/ && ls && TestsDLLEnter.exe')
    pass
