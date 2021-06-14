# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class NEPSE_share_time_obj(scrapy.Item):
    symbol = scrapy.Field()
    time_form = scrapy.Field()
    share_name = scrapy.Field()
    time_list = scrapy.Field()

class Share_Basic_Info(scrapy.Item):
    share_outstanding = scrapy.Field()
    market_price = scrapy.Field()
    percentage_change = scrapy.Field()
    fifty_two_weeks_low =  scrapy.Field()
    fifty_two_weeks_high =  scrapy.Field()
    hundred_eighty_average = scrapy.Field()
    hundred_twenty_average = scrapy.Field()
    one_year_yield = scrapy.Field()
    eps = scrapy.Field()
    eps_value = scrapy.Field()
    pe_ratio = scrapy.Field()
    book_value = scrapy.Field()
    pbv = scrapy.Field()
    percentage_divident = scrapy.Field()
    percentage_divident_value = scrapy.Field()
    percentage_bonus = scrapy.Field()
    percentage_bonus_value = scrapy.Field()
    right_share = scrapy.Field()
    right_share_value = scrapy.Field()
    thirty_day_average_volume = scrapy.Field()
    recorded_date = scrapy.Field()
    share_symbol = scrapy.Field()

