import os
import django
from aiogram.utils.executor import start_webhook

from config.enviroments import WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, PORT
from loader import bot, SSL_CERTIFICATE, sslContext
from src import filters


async def onStartup(dp):
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL,
            certificate=SSL_CERTIFICATE
        )

    filters.setup(dp)


async def onShutdown(dp):
    await dp.storage.close()
    await dp.storage.wait_closed()


def setup_django():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "admin.settings"
    )
    os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': "true"})
    django.setup()


if __name__ == '__main__':
    setup_django()
    from src.handlers import dp
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=onStartup,
        on_shutdown=onShutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=PORT,
        ssl_context=sslContext
    )
