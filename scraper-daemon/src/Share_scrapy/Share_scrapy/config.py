import os
from box import Box
from dotenv import load_dotenv
from os.path import join, dirname

load_dotenv()

BASE_URL = os.environ.get('BASE_URL')

CONFIG = Box({
    "BASE_URL": BASE_URL,
    "MOVING_AVERAGE": f"{BASE_URL}/movingaverage/",
    "SHARE_BASIC_INFO": f"{BASE_URL}/sharebasicinfo/",
    "SHARE_PRICE": f"{BASE_URL}/shareprice/",
    "SHARE": f"{BASE_URL}/share/",
    "SHARE_CATEGORY": f"{BASE_URL}/sharecategory/"
})
