# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from itemadapter import ItemAdapter
from scrapy.utils.serialize import ScrapyJSONEncoder

import Share_scrapy.services.share as share_services
import Share_scrapy.services.moving_average as moving_average_services
import Share_scrapy.services.share_basic_info as share_basic_info_services

from datetime import datetime

class ShareScrapyPipeline:
    def process_item(self, item, spider):
        return item


class DuplicatePipeLine: 
    
    def __init__(self):
        self.time_seen = set()
    
    def process_item(self, item, spider):
        new_time_list = []

        for timeVal in item['time_list']:

            minute_value = int(timeVal['time'].strftime("%M"))
            nearest_multiple_of_five = (5 * round(minute_value/5)) % 60

            t_value = timeVal['time'].replace(minute=nearest_multiple_of_five)
            date_text= t_value.strftime("%m/%d/%Y, %H:%M:%S")

            if date_text in self.time_seen:
                continue
            else:
                self.time_seen.add(date_text)
                new_time_list.append({"time": t_value, "value": timeVal["value"]})

        item['time_list'] = new_time_list

        self.time_seen.clear()
        return item

class Store_Latest_price_data:
    def process_item(self, item, spider):
        latest_data = share_services.get_latest_record_for_share(item["symbol"])

        latest_date =  datetime.strptime(latest_data["date_time"], '%Y-%m-%d %H:%M:%S')

        new_time_list = []

        for timeVal in item['time_list']:
            if(timeVal["time"] > latest_date):
                new_time_list.append(timeVal)
                
        item["time_list"] = new_time_list

        return item

class Save_Share_Price_To_Data_Base:
     def process_item(self, item, spider):
         _encoder = ScrapyJSONEncoder()
         json_encoded_item = _encoder.encode(item)

         share_services.store_share_data(json_encoded_item)
         return item
    

class Save_Share_Data_Mero_Lagani:
    def process_item(self, item, spider):
        _encoder = ScrapyJSONEncoder()

        moving_average_low = {
            "value": item["fifty_two_weeks_low"],
            "movingAverageCategoryId": 1,
            "shareSymbol": item["share_symbol"],
            "record_date": item["recorded_date"]
        }

        moving_average_high = {
            "value" : item["fifty_two_weeks_high"],
            "movingAverageCategoryId": 2,
            "shareSymbol": item["share_symbol"],
            "record_date": item["recorded_date"]
        }

        moving_average_hundred_eighty_average = {
            "value" : item["hundred_eighty_average"],
            "movingAverageCategoryId": 3,
            "shareSymbol": item["share_symbol"],
            "record_date": item["recorded_date"]
        }

        moving_average_hundred_twenty_average = {
            "value" : item["hundred_twenty_average"],
            "movingAverageCategoryId": 4,
            "shareSymbol": item["share_symbol"],
            "record_date": item["recorded_date"]
        }

        moving_average_thirty_day_average_volume = {
            "value" : item["thirty_day_average_volume"],
            "movingAverageCategoryId": 5,
            "shareSymbol": item["share_symbol"],
            "record_date": item["recorded_date"]
        }

        share_basic_info = {
            "share_outstanding": item["share_outstanding"],
            "one_year_yield": item["one_year_yield"],
            "eps": item["eps"],
            "eps_value": item["eps_value"],
            "pe_ratio": item["pe_ratio"],
            "book_value": item["book_value"],
            "pbv": item["pbv"],
            "percentage_divident": item["percentage_divident"],
            "percentage_divident_value": item["percentage_divident_value"],
            "percentage_bonus": item["percentage_bonus"],
            "percentage_bonus_value": item["percentage_bonus_value"],
            "right_share": item["right_share"],
            "right_share_value": item["right_share_value"],
            "record_date": item["recorded_date"],
            "share_symbol": item["share_symbol"]
        }

        json_share_basic_info = _encoder.encode(share_basic_info)

        moving_average_services.store_share_data(_encoder.encode(moving_average_low))
        moving_average_services.store_share_data(_encoder.encode(moving_average_high))
        moving_average_services.store_share_data(_encoder.encode(moving_average_hundred_eighty_average))
        moving_average_services.store_share_data(_encoder.encode(moving_average_hundred_twenty_average))
        moving_average_services.store_share_data(_encoder.encode(moving_average_thirty_day_average_volume))

        share_basic_info_services.store_share_data(json_share_basic_info)

        return item