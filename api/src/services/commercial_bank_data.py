from .share_service import Share_Service

class Commercial_Bank_Services(Share_Service):
    FILE_PATH = "/home/serpant/Desktop/work/share_report/data/commercialBank/"

    def __init__(self):
        super().__init__(self.FILE_PATH)

commercial_bank_services = Commercial_Bank_Services()
