import dao.share_categories as share_categories_dao

def fetch_all():
    return share_categories_dao.fetch_all()

def fetch_all_with_share():
    return share_categories_dao.fetch_all_with_share()
    