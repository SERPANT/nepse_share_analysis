import scrapy
from scrapy import Request
from datetime import date

from Share_scrapy.items import Share_Basic_Info
import Share_scrapy.services.share as share_services
import Share_scrapy.services.share_basic_info as share_basic_info_services

class MerolaganiScrapperSpider(scrapy.Spider):
    ''' Fetches detailed information about a share from Mero lagani site '''
    
    name = 'merolagani_scrapper'
    allowed_domains = ['https://merolagani.com/']

    custom_settings = {
        'ITEM_PIPELINES': {
            'Share_scrapy.pipelines.merolagani_scrapper.save_share_data_mero_lagani.Save_Share_Data_Mero_Lagani': 300,
            }
    }

    def __init__(self):
        ''' Initialization function of the class 

            Set up the share list
        '''

        self.share_list = share_services.fetch_all()

    
    def start_requests(self):
        ''' Generate start url from company list 

            Returns: Generator object (mero lagani company share link) 
        '''

        for company in self.share_list:
            url = 'https://merolagani.com/CompanyDetail.aspx?symbol=' + company["symbol"]

            yield Request(url,callback=self.parse)


    def get_value(self, value1, value2, value3):
        ''' Check to see values in value1, value2 and value3 and return it in a combined way

            Returns value1 + value2 + value3
        '''

        value = ""

        if(value1 != None):
            value = value + value1.strip()

        if(value2 != None):
            value = value + value2.strip()

        if(value3 != None):
            value = value + value3.strip()

        return value

    def parse(self, response):
        ''' Start of the scrapper 

            Returns: Share_Basic_Info object
        '''

        # Extract all the rows. (Rows from the table with id = accordion has the data)
        rows = response.xpath("//*[@id='accordion']/tbody/tr")

        # A Dictionary obj to store all the rows.
        dic = {}
        
        for row in rows:
            field = row.xpath("./th/a/text()").get() or row.xpath("./th/text()").get() 

            value1 =  row.xpath("./td/text()").get()
            value2 = row.xpath("./td/*/text()").get()
            value3 = row.xpath("./td/*/*/text()").get()
            value = self.get_value(value1, value2, value3)

            if(field == None or value == None):
                continue

            dic[field.strip()] = value
            print(field.strip() + " = " + value)
        
        return share_basic_info_services.generate_object(dic)
