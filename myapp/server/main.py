import sys

from .gunicorn import run as gunicorn_runner
from .uvicorn import run as uvicorn_runner

HOST = '127.0.0.1'
PORT = 8000


def run():
    try:
        server = sys.argv[1]
        if server == 'gunicorn':
            server_runner = gunicorn_runner
        else:
            server_runner = uvicorn_runner
    except:
        server_runner = uvicorn_runner

    server_runner(HOST, PORT)
