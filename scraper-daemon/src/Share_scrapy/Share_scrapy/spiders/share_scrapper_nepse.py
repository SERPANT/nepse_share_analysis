import scrapy

from Share_scrapy.items import Nepse_Share_List

import Share_scrapy.config as config

class ShareScrapperNepseSpider(scrapy.Spider):
    name = 'share_scrapper_nepse'
    allowed_domains = ['http://www.nepalstock.com']
    start_urls = ['http://www.nepalstock.com/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'Share_scrapy.pipelines.share_scrapper_nepse.insert_new_share.InsertNewShare': 100,
        },
        'FEED_URI' : "../../../../../data/nepse_share_key_value.json",
        'FEED_FORMAT' : "json"
    }

    def parse(self, response):
        print("=============================", config)

        pass
        # share_options = response.xpath("//*[@id='stockChartSelect']/option")

        # share_list = []

        # for share_info in share_options:
        #     share_symbol = share_info.xpath("./text()").get()
        #     share_number = share_info.xpath("./@value").get()
            
        #     share_list.append({"share_symbol": share_symbol,"share_number": share_number })

        # return share_list
        