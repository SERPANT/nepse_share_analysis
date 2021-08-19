import dao.moving_average_value as moving_average_value_dao
from utils.alchemy_encoder import AlchemyEncoder

def create(moving_average_obj):
    moving_average_value_dao.create(moving_average_obj)


def get_all_latest_for_all_share():
    moving_average_array = moving_average_value_dao.get_all_latest_for_all_share()

    share_grouped_dic = {}

    for moving_average in moving_average_array:
        if moving_average.share_symbol in share_grouped_dic:
            share_grouped_dic[moving_average.share_symbol][moving_average.moving_average_category.name] = str(moving_average.value)
        else:
            share_grouped_dic[moving_average.share_symbol] = {}
            share_grouped_dic[moving_average.share_symbol][moving_average.moving_average_category.name] = str(moving_average.value)

    return share_grouped_dic





    