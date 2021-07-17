import json
from Share_scrapy.utils.https import post, get, put

def store_share_data(share_data):
    post('http://127.0.0.1:5000/api/shareprice/', share_data)


def get_latest_record_for_share(share_symbol):
    response = get(f'http://127.0.0.1:5000/api/shareprice/latest?shareSymbol={share_symbol}')

    return response.json()

def get_share_record(share_symbol):
    response = get(f'http://127.0.0.1:5000/api/share/{share_symbol}')

    return response.json()


def patch_share_record(share):
    print("--------------")
    print("--------------")
    print("--------------")
    print("--------------")
    print(share)
    put('http://127.0.0.1:5000/api/share/', json.dumps(share))
    