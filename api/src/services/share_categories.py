import dao.share_categories as share_categories_dao

import services.moving_average_value as moving_average_value_services 

from utils.alchemy_encoder import AlchemyEncoder

def fetch_all():
    return share_categories_dao.fetch_all()

def fetch_all_with_share():
    category_data = share_categories_dao.fetch_all_with_share()
    moving_average_value_data = moving_average_value_services.get_all_latest_for_all_share()

    dic_category_array = AlchemyEncoder.convert_model_list_to_dic(category_data, ['share_prices', 'moving_average_values'])

    for category in dic_category_array:
        for share in category["share"]:
            share["moving_avearge_values"]= moving_average_value_data[share["symbol"]]
    
    return dic_category_array

    
def create(share_catory_obj):
    return share_categories_dao.create(share_catory_obj)


def fetch_by_name(name):
    return share_categories_dao.fetch_by_name(name)

