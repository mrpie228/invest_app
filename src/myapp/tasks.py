from __future__ import absolute_import, unicode_literals
import logging
from .celery import app
import os
from os import path

logger = logging.getLogger("celery")


@app.task
def parse_crypto():
    # os.system(r'cd c_sharp_scripts/CryptoParse/CryptoProjects/ && ls && mcs CryproParse.cs')
    # os.system(r'cd c_sharp_scripts/CryptoParse/exe/ && ls && mono --aot -O=all CryptoParseDLL.dll')
    # os.system(r'cd c_sharp_scripts/CryptoParse/exe/ && mono TestsDLLEnter.exe')
    pass
@app.task
def parse_stocks():
    pass