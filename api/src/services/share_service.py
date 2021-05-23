from utils import file as file_util

class Share_Service:
    MONTHLY_DATA_FILE_NAME = "monthly.json"
    WEEKLY_DATA_FILE_NAME = "weekly.json"
    DAILY_DATA_FILE_NAME = "daily.json"
    QUATERLY_DATA_FILE_NAME = "quaterly.json"
    YEARLY_DATA_FILE_NAME = "yearly.json"

    FILE_PATH = None

    def __init__(self, filePath):
        self.FILE_PATH = filePath

    def fetch_monthly_data(self):
        return file_util.read_file(self.FILE_PATH +  self.MONTHLY_DATA_FILE_NAME)

    def fetch_weekly_data(self):
        return file_util.read_file(self.FILE_PATH + self.WEEKLY_DATA_FILE_NAME)

    def fetch_daily_data(self):
        return file_util.read_file(self.FILE_PATH + self.DAILY_DATA_FILE_NAME)
    
    def fetch_quaterly_data(self):
        return file_util.read_file(self.FILE_PATH + self.QUATERLY_DATA_FILE_NAME)
    
    def fetch_yearly_data(self):
        return file_util.read_file(self.FILE_PATH + self.YEARLY_DATA_FILE_NAME)

