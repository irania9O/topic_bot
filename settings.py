from os import environ
from dotenv import load_dotenv
load_dotenv()

# Load environment variables
PROXY_ENABLED = environ.get('PROXY_ENABLED', False)
PROXY_SCHEME = environ.get('PROXY_SCHEME', 'http')
PROXY_HOST = environ.get('PROXY_HOST', '127.0.0.1')
PROXY_PORT = environ.get('PROXY_PORT', 8000)
PROXY_USERNAME = environ.get('PROXY_USERNAME', None)
PROXY_PASSWORD = environ.get('PROXY_PASSWORD', None)

API_ID = environ.get('API_ID', None)
API_HASH = environ.get('API_HASH', None)
BOT_TOKEN = environ.get('BOT_TOKEN', None)

proxy = {}
if PROXY_ENABLED == 'True':
   proxy = {
     "scheme": PROXY_SCHEME,  # "socks4", "socks5" and "http" are supported
     "hostname": PROXY_HOST,
     "port": int(PROXY_PORT),
     "username": PROXY_USERNAME,
     "password": PROXY_PASSWORD
    } 