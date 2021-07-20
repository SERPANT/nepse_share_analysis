from Share_scrapy.utils.https import post

from Share_scrapy.config import CONFIG

def store_share_data(moving_average):
    post(CONFIG.MOVING_AVERAGE, moving_average)
