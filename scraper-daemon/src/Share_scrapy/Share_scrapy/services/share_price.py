from Share_scrapy.utils.https import post, get

from Share_scrapy.config import CONFIG

def store_share_price_data(share_data):
    post(CONFIG.SHARE_PRICE, share_data)


def get_latest_record_for_share(share_symbol):
    response = get(f'{CONFIG.SHARE_PRICE}latest?shareSymbol={share_symbol}')

    return response.json()
