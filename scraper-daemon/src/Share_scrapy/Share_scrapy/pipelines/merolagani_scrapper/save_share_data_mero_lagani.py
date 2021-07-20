from scrapy.utils.serialize import ScrapyJSONEncoder

import Share_scrapy.services.moving_average as moving_average_services
import Share_scrapy.services.share_basic_info as share_basic_info_services

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
        