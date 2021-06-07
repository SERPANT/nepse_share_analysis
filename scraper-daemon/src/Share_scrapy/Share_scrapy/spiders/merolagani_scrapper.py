import scrapy

from Share_scrapy.items import Share_Basic_Info

class MerolaganiScrapperSpider(scrapy.Spider):
    name = 'merolagani_scrapper'
    allowed_domains = ['https://merolagani.com/']
    start_urls = [
        'https://merolagani.com/CompanyDetail.aspx?symbol=hbl',
        "https://merolagani.com/CompanyDetail.aspx?symbol=ADBL"
    ]

    custom_settings = {
        'FEED_URI' : "../../../../../data/test/share_info.json",
        'FEED_FORMAT' : "json"
    }

    def get_value(self, value1, value2, value3):
        value = ""

        if(value1 != None):
            value = value + value1.strip()

        if(value2 != None):
            value = value + value2.strip()

        if(value3 != None):
            value = value + value3.strip()

        return value

    def parse(self, response):
        rows = response.xpath("//*[@id='accordion']/tbody/tr")

        dic = {}
        for row in rows:
            field = row.xpath("./th/a/text()").get() or row.xpath("./th/text()").get() 

            value1 =  row.xpath("./td/text()").get()
            value2 = row.xpath("./td/*/text()").get()
            value3 = row.xpath("./td/*/*/text()").get()
            value = self.get_value(value1, value2, value3)

            if(field == None or value == None):
                continue

            dic[field.strip()] = value
            print(field.strip() + " = " + value)
        
        share_info_obj = Share_Basic_Info()

        share_info_obj["share_outstanding"] = dic["Shares Outstanding"]
        share_info_obj["market_price"] = dic["Market Price"]
        share_info_obj["percentage_change"] = dic["% Change"]

        low, high = dic["52 Weeks High - Low"].split("-")
        share_info_obj["fifty_two_weeks_low"] = low
        share_info_obj["fifty_two_weeks_high"] = high
        share_info_obj["hundred_eighty_average"] = dic["180 Day Average"]
        share_info_obj["hundred_twenty_average"] = dic["120 Day Average"]
        share_info_obj["one_year_yield"] = dic["1 Year Yield"]
        
        share_info_obj["eps"] = dic["EPS"]
        share_info_obj["eps_value"] = dic["EPS"].split("(")[0]

        share_info_obj["pe_ratio"] = dic["P/E Ratio"]
        share_info_obj["book_value"] = dic["Book Value"]
        share_info_obj["pbv"] = dic["PBV"]

        share_info_obj["percentage_divident"] = dic["% Dividend"]
        share_info_obj["percentage_divident_value"] = dic["% Dividend"].split("(")[0]

        share_info_obj["percentage_bonus"] = dic["% Bonus"]
        share_info_obj["percentage_bonus_value"] = dic["% Bonus"].split("(")[0]

        share_info_obj["right_share"] = dic["Right Share"]
        share_info_obj["right_share_value"] = dic["Right Share"].split("(")[0]
        share_info_obj["thirty_day_average_volume"] = dic["30-Day Avg Volume"]


        return share_info_obj

