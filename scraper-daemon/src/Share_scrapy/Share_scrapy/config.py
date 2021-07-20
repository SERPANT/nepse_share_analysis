from box import Box
from dotenv import dotenv_values

CONFIG = Box({
    "BASE_URL": "http://127.0.0.1:5000/api",
    "MOVING_AVERAGE": "http://127.0.0.1:5000/api/movingaverage/",
    "SHARE_BASIC_INFO": "http://127.0.0.1:5000/api/sharebasicinfo/",
    "SHARE_PRICE": "http://127.0.0.1:5000/api/shareprice/",
    "SHARE": "http://127.0.0.1:5000/api/share/"
})
