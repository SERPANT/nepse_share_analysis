import dao.share_price_over_time as share_price_over_time_dao

def fetch_range_by_share(start_date, end_date, share_symbol, share_name):
    data = share_price_over_time_dao.fetch_range_by_share(start_date, end_date, share_symbol, share_name)

    return data



def create(share_price_obj):
    return share_price_over_time_dao.create(share_price_obj)
