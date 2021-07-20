from datetime import datetime

import Share_scrapy.services.share_price as share_price_services

class Store_Latest_price_data:
    def process_item(self, item, spider):
        latest_data = share_price_services.get_latest_record_for_share(item["symbol"])

        if(latest_data == None):
             return item

        latest_date =  datetime.strptime(latest_data["date_time"], '%Y-%m-%d %H:%M:%S')
        new_time_list = []

        for timeVal in item['time_list']:
            if(timeVal["time"] > latest_date):
                new_time_list.append(timeVal)
                
        item["time_list"] = new_time_list

        return item
        