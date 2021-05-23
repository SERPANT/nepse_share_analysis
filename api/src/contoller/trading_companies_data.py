FILE_PATH = "/home/serpant/Desktop/work/share_report/data/nepse_month_data.json"

from utils import file as file_util

def fetch_data():
    return file_util.read_file(FILE_PATH)