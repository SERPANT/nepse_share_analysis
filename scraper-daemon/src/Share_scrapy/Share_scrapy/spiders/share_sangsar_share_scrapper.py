import scrapy

from Share_scrapy.constants.moving_average_links import MOVING_AVERAGE_LINKS

class Share_Sangsar_Share_Scrapper(scrapy.Spider):
    name = 'share_sangsar_share_scrapper'
    allowed_domains = ['www.sharesansar.com']
    start_urls = MOVING_AVERAGE_LINKS["CommercialBankShare"]

    def parse(self, response):
