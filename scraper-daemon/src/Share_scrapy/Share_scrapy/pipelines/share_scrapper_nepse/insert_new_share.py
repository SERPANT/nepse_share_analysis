
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

import Share_scrapy.services.share as share_services

class InsertNewShare:
    def process_item(self, item, spider):
        if item["share_symbol"] == None or item["share_symbol"] == "":
            raise DropItem("Already setup")
        
        share_symbol = item["share_symbol"].upper()

        share_record = share_services.get_share_record(share_symbol)

        if(share_record == None):
            #share_services.get_share_name_from_symbol(share_symbol)
            #share_services.create_new_share_record()

            # go to mero share
            # pull data
            # if not present send it to the file
            # if not then create

            return item

        if(share_record["share_number_nepse"] == None):
            share_services.patch_share_record(
                {"symbol": share_symbol, "share_number": item["share_number"]})

        raise DropItem("Already setup")
    