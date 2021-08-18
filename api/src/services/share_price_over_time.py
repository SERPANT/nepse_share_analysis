import json
from datetime import datetime

import services.share as share_services
import dao.share_price_over_time as share_price_over_time_dao

from utils import http

def fetch_range_by_share(start_date, end_date, share_symbol, share_name):
    data = share_price_over_time_dao.fetch_range_by_share(start_date, end_date, share_symbol, share_name)

    return data

def create(share_price_obj):
    return share_price_over_time_dao.create(share_price_obj)


def fetch_latest_record(share_symbol):
    return share_price_over_time_dao.fetch_latest_record(share_symbol)


def fetch_daily_data_for_share(share_symbol, share_name):
    share = share_services.fetch_by_symbol(share_symbol)
    share_number = share.share_number_nepse

    # share_number = 360

    url = f"http://www.nepalstock.com/company/graphdata/{share_number}/D" 

    response = http.get(url)

    time_seen = []
    time_list = []

    try:
        json_data = response.json()
    except:
        print("===================================== ", response.text)
        
        response_dic = {
            "share": share_symbol,
            "shareName": share_name,
            "timeList": []
            }

        return response_dic

    for data in json_data:
        date_time_obj = datetime.fromtimestamp(data[0]/1000)
        new_date_obj = date_time_obj.replace(second=0)

        min_value = int(new_date_obj.strftime("%M"))

        nearest_multiple_of_five = (5 * round(min_value/5)) % 60

        t_value = new_date_obj.replace(minute=nearest_multiple_of_five)

        date_text = t_value.strftime("%Y-%m-%d %H:%M:%S")

        if date_text in time_seen:
            continue

        time_seen.append(date_text)
        dic = {"date_time": date_text, "price": data[1]}

        time_list.append(dic)


    response_dic = {
        "share": share_symbol,
        "shareName": share_name,
        "timeList": time_list
    }

    return response_dic
