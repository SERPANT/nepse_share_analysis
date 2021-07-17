import scrapy


class ShareNepseSpider(scrapy.Spider):
    name = 'share_nepse'
    allowed_domains = ['http://www.nepalstock.com/']
    start_urls = ['http://www.nepalstock.com/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'Share_scrapy.pipelines.Insert_New_Share': 300,
        }
    }

    def parse(self, response):
        share_options = response.xpath("//*[@id='stockChartSelect']/option")

        share_list = []

        for share_info in share_options:
            share_symbol = share_info.xpath("./text()").get()
            share_number = share_info.xpath("./@value").get()
            
            share_list.append({"share_symbol": share_symbol, "share_number": share_number})

        return share_list
        