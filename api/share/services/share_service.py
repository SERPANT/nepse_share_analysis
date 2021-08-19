from utils import file as file_util
from constants.data_folder_name import DATA_FOLDER_NAME
class Share_Service:

    MONTHLY_DATA_FILE_NAME = "monthly.json"
    WEEKLY_DATA_FILE_NAME = "weekly.json"
    DAILY_DATA_FILE_NAME = "daily.json"
    QUATERLY_DATA_FILE_NAME = "quaterly.json"
    YEARLY_DATA_FILE_NAME = "yearly.json"

    FILE_PATH = "/home/serpant/Desktop/work/share_report/data/"

    def get_file_path_by_category(self, category): 
        return self.FILE_PATH + DATA_FOLDER_NAME[category]

    def fetch_monthly_data(self, category):
        file_path = self.get_file_path_by_category(category)
        return file_util.read_file(file_path + "/" + self.MONTHLY_DATA_FILE_NAME)

    def fetch_weekly_data(self, category):
        file_path = self.get_file_path_by_category(category)
        return file_util.read_file(file_path + "/" + self.WEEKLY_DATA_FILE_NAME)

    def fetch_daily_data(self, category):
        file_path = self.get_file_path_by_category(category)
        return file_util.read_file(file_path + "/" +self.DAILY_DATA_FILE_NAME)
    
    def fetch_quaterly_data(self, category):
        file_path = self.get_file_path_by_category(category)
        return file_util.read_file(file_path +"/" + self.QUATERLY_DATA_FILE_NAME)
    
    def fetch_yearly_data(self, category):
        file_path = self.get_file_path_by_category(category)
        return file_util.read_file(file_path +"/"+ self.YEARLY_DATA_FILE_NAME)


share_services = Share_Service()
