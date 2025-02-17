from os import environ

# Load environment variables
PROXY = environ.get('PROXY_ENABLED', False)
PROXY_SCHEME = environ.get('PROXY_SCHEME', 'http')
PROXY_HOST = environ.get('PROXY_HOST', '127.0.0.1')
PROXY_PORT = environ.get('PROXY_PORT', 8000)
PROXY_USERNAME = environ.get('PROXY_USERNAME', None)
PROXY_PASSWORD = environ.get('PROXY_PASSWORD', None)

proxy = {}
if PROXY == 'True':
   proxy = {
     "scheme": PROXY_SCHEME,  # "socks4", "socks5" and "http" are supported
     "hostname": PROXY_HOST,
     "port": PROXY_PORT,
     "username": PROXY_USERNAME,
     "password": PROXY_PASSWORD
    } 