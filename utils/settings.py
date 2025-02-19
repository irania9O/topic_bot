from os import environ
from dotenv import load_dotenv
load_dotenv()

PROXY = environ.get('PROXY', '"socks5://127.0.0.1:2080')
BOT_TOKEN = environ.get('BOT_TOKEN', None)
POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD", None)
