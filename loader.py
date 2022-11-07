import ssl

from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from config import enviroments


bot = Bot(token=enviroments.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

sslContext = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
SSL_CERTIFICATE = open(enviroments.CERT, "rb").read()
sslContext.load_cert_chain(enviroments.CERT, enviroments.PKEY)

