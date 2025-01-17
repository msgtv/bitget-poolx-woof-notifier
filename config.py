from dotenv import load_dotenv

import os

load_dotenv('.env')

api_key = os.getenv("api_key")
secret_key = os.getenv("secret_key")
passphrase = os.getenv("passphrase")
CHAT_ID = os.getenv('CHAT_ID')
BOT_API = os.getenv('BOT_API')

POOL_WOOF_PRODUCT_ID = "1263054816390041600"

SPOT_ASSETS_URL = "/api/v2/spot/account/assets"

WOOF_COUNT_TO_INFORM = 4000

POOLX_URL = 'https://www.bitgetapps.com/ru/events/poolx/1263054816390041600?appTheme=dark&appVersion=2.49.0&clacCode=2FQ370CK&productSubId=1263054816419401728&time=1737135973913'
