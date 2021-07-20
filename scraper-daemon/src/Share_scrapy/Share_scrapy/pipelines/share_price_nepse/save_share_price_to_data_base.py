from scrapy.utils.serialize import ScrapyJSONEncoder

import Share_scrapy.services.share_price as share_price_services

class Save_Share_Price_To_Data_Base:
     def process_item(self, item, spider):
         _encoder = ScrapyJSONEncoder()
         json_encoded_item = _encoder.encode(item)

         share_price_services.store_share_price_data(json_encoded_item)
         return item
         