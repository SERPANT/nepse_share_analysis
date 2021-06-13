from Share_scrapy.utils.https import post

def store_share_data(share_data):
    post('http://127.0.0.1:5000/api/shareprice/', share_data)