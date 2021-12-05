from threading import *
from core import *

from bots import telegram, viber

viber_thread = Thread(target=viber.start_bot)

viber_thread.start()
telegram.start_bot()

