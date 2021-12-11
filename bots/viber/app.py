from .loader import app, viber, core
from . import handlers
from .data import config


def start_bot():
    context = ('server.crt', 'server.key')
    app.run(port=8087)
