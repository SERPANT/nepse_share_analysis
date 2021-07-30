import scrapy


class ShareFloorsheetNepseSpider(scrapy.Spider):
    name = 'share_floorsheet_nepse'
    allowed_domains = ['http://www.nepalstock.com/main/floorsheet/']
    start_urls = ['http://http://www.nepalstock.com/main/floorsheet/']

    def __init__(self, symbol):
        http://www.nepalstock.com/main/floorsheet/index/1/?contract-no=&stock-symbol=LBBL&buyer=&seller=&_limit=500



    def parse(self, response):
        pass
