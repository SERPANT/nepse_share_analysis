from Share_scrapy.utils.https import post

from Share_scrapy.config import CONFIG

def store_share_data(share_basic_info):
    post(CONFIG.SHARE_BASIC_INFO, share_basic_info)


def generate_object(merolagani_merolagani_dic): 
    ''' 
        Generates a basic share info object. Note: only works if passed merolagani_dic object from mero lagani scrapper.

        Parameter: 
            - merolagani_dic_obj: Dic created while running mero lagani scrapper.

        Returns: Share_basic_info object
    '''

    share_info_obj = Share_Basic_Info()
    share_info_obj["share_outstanding"] = merolagani_dic["Shares Outstanding"]
    share_info_obj["market_price"] = merolagani_dic["Market Price"]
    share_info_obj["percentage_change"] = merolagani_dic["% Change"]

    low, high = merolagani_dic["52 Weeks High - Low"].split("-")
    share_info_obj["fifty_two_weeks_low"] = float(str(low).replace(',', '')) 
    share_info_obj["fifty_two_weeks_high"] = float(str(high).replace(',', '')) 
    share_info_obj["hundred_eighty_average"] = float(str(merolagani_dic["180 Day Average"]).replace(',', ''))
    share_info_obj["hundred_twenty_average"] = float(str(merolagani_dic["120 Day Average"]).replace(',', ''))
    share_info_obj["one_year_yield"] = merolagani_dic["1 Year Yield"]
        
    share_info_obj["eps"] = merolagani_dic["EPS"]
    share_info_obj["eps_value"] = merolagani_dic["EPS"].split("(")[0]

    share_info_obj["pe_ratio"] = float(str(merolagani_dic["P/E Ratio"]).replace(',', ''))
    share_info_obj["book_value"] = float(str(merolagani_dic["Book Value"]).replace(',', ''))
    share_info_obj["pbv"] = merolagani_dic["PBV"]

    share_info_obj["percentage_divident"] = merolagani_dic["% Dividend"]
    share_info_obj["percentage_divident_value"] = merolagani_dic["% Dividend"].split("(")[0]

    share_info_obj["percentage_bonus"] = merolagani_dic["% Bonus"]
    share_info_obj["percentage_bonus_value"] = merolagani_dic["% Bonus"].split("(")[0]

    share_info_obj["right_share"] = merolagani_dic["Right Share"]
    share_info_obj["right_share_value"] = merolagani_dic["Right Share"].split("(")[0]
    share_info_obj["thirty_day_average_volume"] = float(str(merolagani_dic["30-Day Avg Volume"]).replace(',', ''))
    share_info_obj["recorded_date"] = date.today()
    share_info_obj["share_symbol"] = ((response.url.split("="))[1]).upper()

    return share_info_obj
