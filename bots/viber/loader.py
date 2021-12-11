from flask import Flask
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from core import Core
from .data import config

app = Flask(__name__)
viber = Api(BotConfiguration(
    name='PythonSampleBot',
    avatar='http://site.com/avatar.jpg',
    auth_token=config.BOT_TOKEN
))
core = Core("Viber")
