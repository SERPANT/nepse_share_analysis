from Share_scrapy.utils.https import post

def store_share_data(moving_average):
    post('http://127.0.0.1:5000/api/movingaverage/', moving_average)
