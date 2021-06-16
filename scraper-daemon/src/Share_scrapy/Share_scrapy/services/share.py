from Share_scrapy.utils.https import post, get

def store_share_data(share_data):
    post('http://127.0.0.1:5000/api/shareprice/', share_data)


def get_latest_record_for_share(share_symbol):
    response = get(f'http://127.0.0.1:5000/api/shareprice/latest?shareSymbol={share_symbol}')

    return response.json()
    