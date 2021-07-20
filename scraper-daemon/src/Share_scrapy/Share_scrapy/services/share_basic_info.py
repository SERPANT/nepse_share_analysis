from Share_scrapy.utils.https import post

from Share_scrapy.config import CONFIG

def store_share_data(share_basic_info):
    post(CONFIG.SHARE_BASIC_INFO, share_basic_info)
