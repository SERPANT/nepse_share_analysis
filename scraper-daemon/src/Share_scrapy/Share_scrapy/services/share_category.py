import json

from Share_scrapy.config import CONFIG
from Share_scrapy.utils.https import get, post

def fetch_by_name(name):
    print(f"{CONFIG.SHARE_CATEGORY}name?name={name}")
    response = get(f"{CONFIG.SHARE_CATEGORY}name?name={name}")
    
    return response.json()


def create(share_category):
    post(CONFIG.SHARE_CATEGORY, json.dumps(share_category))