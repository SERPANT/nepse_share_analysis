from Share_scrapy.utils.https import post

def store_share_data(share_basic_info):
    post('http://127.0.0.1:5000/api/sharebasicinfo/', share_basic_info)
