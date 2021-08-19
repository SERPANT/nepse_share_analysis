
import requests
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy import Selector

import Share_scrapy.services.share as share_services
import Share_scrapy.services.share_category as share_category_services

class InsertNewShare:
    def process_item(self, item, spider):
        if item["share_symbol"] == None or item["share_symbol"] == "":
            raise DropItem("Already setup")
        
        share_symbol = item["share_symbol"].upper()

        share_record = share_services.get_share_record(share_symbol)

        if(share_record == None):
            url = f"https://merolagani.com/CompanyDetail.aspx?symbol={share_symbol}"
            
            request_object = requests.get(url)
            response_object = Selector(request_object )

            share_name = response_object.xpath("//*[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_companyName']/text()").get()

            if share_name == None: 
                return item

            share_category = (response_object.xpath("//*[@id='accordion']/tbody/tr/td/text()").get()).strip()

            share_category_data = share_category_services.fetch_by_name(share_category)

            if share_category_data == None:
                return item
                # share_category_services.create([{
                #     "name": share_category
                # }])

                # raise DropItem("Category created")


            share_services.create_new_share_record([{
                "name": share_name,
                "symbol": share_symbol,
                "shareCategoryId": share_category_data["id"],
                "share_number": item["share_number"]
            }])

            raise DropItem("Share created")

        if(share_record["share_number_nepse"] == None):
            share_services.patch_share_record(
                {"symbol": share_symbol, "share_number": item["share_number"]})

        raise DropItem("Already setup")
    