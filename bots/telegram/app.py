from aiogram import executor

from bots.telegram.loader import dp
from bots.telegram import middlewares, filters, handlers
from bots.telegram.utils.notify_admins import on_startup_notify
from bots.telegram.utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


def start_bot():
    executor.start_polling(dp, on_startup=on_startup)


