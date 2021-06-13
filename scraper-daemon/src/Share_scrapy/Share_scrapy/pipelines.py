# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.utils.serialize import ScrapyJSONEncoder

import Share_scrapy.services.share as share_services

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

class Save_Share_Price_To_Data_Base:
     def process_item(self, item, spider):
         _encoder = ScrapyJSONEncoder()
         json_encoded_item = _encoder.encode(item)

         share_services.store_share_data(json_encoded_item)

         return item