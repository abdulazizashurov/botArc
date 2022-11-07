import os
from dotenv import load_dotenv

load_dotenv()
# Settings for Bot
BOT_TOKEN: str = os.getenv('BOT_TOKEN')
GROUP_ID: str = os.getenv('GROUP_ID')
SLEEP_TIME: float = .2

# payments
CLICK = os.getenv('CLICK')

# Settings for web
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')
SECRET_KEY: str = os.getenv('SECRET_KEY')
DEBUG = True

DATABASE = os.getenv('DATABASE')
PGUSER = os.getenv('PGUSER')
PGPASSWORD = os.getenv('PGPASSWORD')
DBHOST = os.getenv('DBHOST')


# Webhook
HOST = os.getenv("HOST")
PORT: int = 8443
WEBAPP_HOST = "0.0.0.0"
WEBHOOK_PATH = f"/bot/{BOT_TOKEN}"
WEBHOOK_URL = f"https://{HOST}:{PORT}{WEBHOOK_PATH}"  # Server

CERT = "cert.pem"
PKEY = "pkey.pem"

