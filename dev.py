import os
import django

from src import filters


async def onStart(dp):
    filters.setup(dp)
    print("Project start...")


async def onShootdown(dp):
    print("Project shootdown...")


def setupDjango():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "admin.settings"
    )
    os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': "true"})
    django.setup()


if __name__ == "__main__":
    setupDjango()
    from src.handlers import dp
    from aiogram.utils import executor

    executor.start_polling(dp, on_startup=onStart, on_shutdown=onShootdown)
