from bitget.bitget_api import BitgetApi
from bitget.exceptions import BitgetAPIException

from config import SPOT_ASSETS_URL


def get_available_coins(client: BitgetApi):
    try:
        url = SPOT_ASSETS_URL
        params = {'coin': 'WOOF'}
        res = client.get(url, params)

        count = float(res['data'][0]['available'])

        return count
    except BitgetAPIException as e:
        raise
