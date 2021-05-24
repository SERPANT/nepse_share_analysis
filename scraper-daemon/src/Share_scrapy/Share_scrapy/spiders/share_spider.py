import json
import scrapy
from scrapy import Request
from datetime import datetime
import sys
import getopt

from Share_scrapy.items import NEPSE_share_time_obj
from Share_scrapy.constants.website_link import START_URL
from Share_scrapy.utils.cmd_args import parse_named_command_line_args

class ShareSpiderSpider(scrapy.Spider):
    name = 'share_spider'
    allowed_domains = ['http://www.nepalstock.com/']
    time = None

    def __init__(self, category = '', time = ''):
        self.time = time
        shares_info = START_URL[category]
        self.share_list = shares_info.links

    @classmethod
    def update_settings(cls, settings):
        arguments = parse_named_command_line_args(sys.argv[2:], 'a:') 
        share_info = START_URL[arguments["category"]]

        custom_settings = {
            'FEED_URI' : share_info.file_locaion[arguments['time']],
            'FEED_FORMATE' : "json"
            }

        settings.setdict(custom_settings, priority='spider')

    def start_requests(self):
        for company in self.share_list:
            url = 'http://www.nepalstock.com/company/graphdata/' + str(company["value"]) + "/" + self.time 
            yield Request(url,callback=self.parse)
    
    def find_company_by_value(self, value):
        for company in self.share_list:
            if company["value"] == value:
                return company


    def parse(self, response):
        body = response.body
        live_market_data = json.loads(body)
        company_value = int(response.url.split('/')[5])
        time_form = response.url.split('/')[6]

        company_obj = self.find_company_by_value(company_value)
        
        nepse_share_time_obj = NEPSE_share_time_obj()
        nepse_share_time_obj["symbol"] = company_obj["symbol"]
        nepse_share_time_obj["time_form"] = time_form
        nepse_share_time_obj["share_name"] = company_obj["name"]
            
        time_list = []

        for data in live_market_data:
            date_time_obj = datetime.fromtimestamp(data[0]/1000)
            new_date_obj = date_time_obj.replace(second=0)
            dic = {"time": new_date_obj, "value": data[1]}
            
            time_list.append(dic)
        
        nepse_share_time_obj["time_list"] = time_list

        return nepse_share_time_obj
