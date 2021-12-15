import sys
import json
import getopt
import scrapy
from scrapy import Request
from datetime import datetime

from Share_scrapy.items import NEPSE_share_time_obj
from Share_scrapy.constants import website_link
from Share_scrapy.utils.cmd_args import parse_named_command_line_args
import Share_scrapy.services.share as share_services

class SharePriceNepseSpider(scrapy.Spider):
    ''' A scrapy spider that fetches the time series data for each share.'''

    name = 'share_price_nepse_spider'
    allowed_domains = ['http://www.nepalstock.com/']
    time = None

    custom_settings = {
        'ITEM_PIPELINES': {
            'Share_scrapy.pipelines.share_price_nepse.duplicate_pipeline.DuplicatePipeLine': 300,
            'Share_scrapy.pipelines.share_price_nepse.store_latest_price_data.Store_Latest_price_data': 400,
            'Share_scrapy.pipelines.share_price_nepse.save_share_price_to_data_base.Save_Share_Price_To_Data_Base': 500
            }
        }

    def __init__(self, time_val = ''):

        # fetching time value as year, day, month, quater
        self.time = time_val

        # set the url links in share_list
        self.share_list = share_services.fetch_all()

    def start_requests(self):

        # generate start url from company list
        for company in self.share_list:
            url = 'http://www.nepalstock.com/company/graphdata/' + str(company["share_number_nepse"]) + "/" + self.time 
            yield Request(url,callback=self.parse)

    
    def find_company_by_value(self, value):
        ''' Given a share number find the Nepse company'''

        for company in self.share_list:
            if company["share_number_nepse"] == value:
                return company


    def parse(self, response):
        ''' Start of the spider '''
        
        body = response.body
        live_market_data = json.loads(body)
        company_value = int(response.url.split('/')[5])

        company_obj = self.find_company_by_value(company_value)

        nepse_share_time_obj = NEPSE_share_time_obj()
        nepse_share_time_obj["symbol"] = company_obj["symbol"]
            
        time_list = []

        for data in live_market_data:
            date_time_obj = datetime.fromtimestamp(data[0]/1000)
            new_date_obj = date_time_obj.replace(second=0)
            dic = {"time": new_date_obj, "value": data[1]}
            
            time_list.append(dic)
        
        nepse_share_time_obj["time_list"] = time_list

        return nepse_share_time_obj
