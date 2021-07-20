import json

from Share_scrapy.utils.https import post, get, put

from Share_scrapy.config import CONFIG


def get_share_record(share_symbol):
    response = get(f'{CONFIG.SHARE}{share_symbol}')

    return response.json()


def patch_share_record(share):
    put(CONFIG.SHARE, json.dumps(share))


def create_new_share_record(share):
    post(CONFIG.SHARE, json.dumps(share))


def get_share_name_from_symbol(share_symbol):
    response = get(f'https://merolagani.com/CompanyDetail.aspx?symbol={share_symbol}')

    print(response.xpath("//*[@id='stockChartSelect']/option"))

    