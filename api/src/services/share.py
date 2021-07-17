import dao.share as share_dao

def create(share):
    share_dao.create(share)

def update(symbol, share_number):
    share_dao.update_share_number(symbol, share_number)


def fetch_by_symbol(symbol):
    return share_dao.fetch_by_symbol(symbol)
    