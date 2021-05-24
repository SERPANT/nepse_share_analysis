# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ShareScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class NEPSE_share_time_obj(scrapy.Item):
    symbol = scrapy.Field()
    time_form = scrapy.Field()
    share_name = scrapy.Field()
    time_list = scrapy.Field()
