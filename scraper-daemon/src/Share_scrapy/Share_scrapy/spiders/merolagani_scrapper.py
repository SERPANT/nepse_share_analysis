import scrapy
from datetime import date

from Share_scrapy.items import Share_Basic_Info

class MerolaganiScrapperSpider(scrapy.Spider):
    name = 'merolagani_scrapper'
    allowed_domains = ['https://merolagani.com/']
    start_urls =  [#"https://merolagani.com/CompanyDetail.aspx?symbol=ADBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=BOKL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=CCBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=CZBIL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=CBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=EBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=GBIME",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=HBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=KBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=LBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=MBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=MEGA",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=NABIL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=NBB",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=NBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=NCCB",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=NIB",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SBI",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=NICA",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=NMB",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=PRVU",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=PCBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SANIMA",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SCB",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SRBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=CORBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=DBBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=EDBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=GDBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=GBBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=GRDBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=JBBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=KSBBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=KADBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=KRBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=LBBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=MLBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=MDB",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=MNBBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=NABBC",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=NCDB",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SHBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SBBLJ",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SAPDBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SADBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SHINE",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SINDU",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=TMDBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=BFC",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=CMB",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=CFCL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=CEFL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=CFL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=GFCL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=GMFIL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=GUFL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=ICFC",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=JFL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=LFC",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=MFIL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=MPFL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=NFS",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=NSM",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=PFL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=PROFL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=RLFL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SFCL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SIFC",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SFFIL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SYFL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=UFL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=AKBSL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=AMFI",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=ALBSL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=CBBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=DDBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=FMDBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=KMCDB",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=NLBBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=NUBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=RMDC",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SKBBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SLBBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SMFDB",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SWBBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=MLBBL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=LLBS",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=MMFDB",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=JSLBB",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=WOMI",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=VLBS",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=RSDC",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=NMBMF",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=MERO",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=NMFBS",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SLBS",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=GMFBS",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=CLBSL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=ILBS",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=FOWAD",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=SMATA",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=MSLB",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=GILB",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=SMB",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=GBLBS",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=MLBSL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=GLBSL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=NICLBSL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=SLBSL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=SDLBSL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=SMFBS",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=SABSL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=ACLBSL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=USLB",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=SNLB",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=KLBSL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=MEROPO",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=OHL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=SHL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=TRH",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=CGH",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=AHPC",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=BPCL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=CHCL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=NHPC",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=SHPC",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=RHPC",
   "https://merolagani.com/CompanyDetail.aspx?symbol=HURJA",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=AKPL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=BARUN",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=API",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=NGPL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=SJCL",
  "https://merolagani.com/CompanyDetail.aspx?symbol=RHPL"
#   "https://merolagani.com/CompanyDetail.aspx?symbol=UMHL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=DHPL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=ALICL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=GLICL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=LICN",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=NLIC",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=NLICL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=PLIC",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=SLICL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=JLI",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=RLI",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=PLI",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=EIC",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=HGI",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=LGIL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=NICL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=NIL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=NLG",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=PIC",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=PICL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=SIC",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=SICL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=SIL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=UIC",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=PRIN",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=RBCL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=IGI",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=AIL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=SGI",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=GIC",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=BBC",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=STC",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=BNL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=BNT",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=HDL",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=NLO",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=RJM",
#   "https://merolagani.com/CompanyDetail.aspx?symbol=UNL",
#  "https://merolagani.com/CompanyDetail.aspx?symbol=SHIVM"
  ]

    custom_settings = {
         'ITEM_PIPELINES': {
            'Share_scrapy.pipelines.Save_Share_Data_Mero_Lagani': 300,
            }
    }

    def get_value(self, value1, value2, value3):
        value = ""

        if(value1 != None):
            value = value + value1.strip()

        if(value2 != None):
            value = value + value2.strip()

        if(value3 != None):
            value = value + value3.strip()

        return value

    def parse(self, response):
        rows = response.xpath("//*[@id='accordion']/tbody/tr")

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
        
        share_info_obj = Share_Basic_Info()

        share_info_obj["share_outstanding"] = dic["Shares Outstanding"]
        share_info_obj["market_price"] = dic["Market Price"]
        share_info_obj["percentage_change"] = dic["% Change"]

        low, high = dic["52 Weeks High - Low"].split("-")
        share_info_obj["fifty_two_weeks_low"] = float(str(low).replace(',', '')) 
        share_info_obj["fifty_two_weeks_high"] = float(str(high).replace(',', '')) 
        share_info_obj["hundred_eighty_average"] = float(str(dic["180 Day Average"]).replace(',', ''))
        share_info_obj["hundred_twenty_average"] = float(str(dic["120 Day Average"]).replace(',', ''))
        share_info_obj["one_year_yield"] = dic["1 Year Yield"]
        
        share_info_obj["eps"] = dic["EPS"]
        share_info_obj["eps_value"] = dic["EPS"].split("(")[0]

        share_info_obj["pe_ratio"] = float(str(dic["P/E Ratio"]).replace(',', ''))
        share_info_obj["book_value"] = float(str(dic["Book Value"]).replace(',', ''))
        share_info_obj["pbv"] = dic["PBV"]

        share_info_obj["percentage_divident"] = dic["% Dividend"]
        share_info_obj["percentage_divident_value"] = dic["% Dividend"].split("(")[0]

        share_info_obj["percentage_bonus"] = dic["% Bonus"]
        share_info_obj["percentage_bonus_value"] = dic["% Bonus"].split("(")[0]

        share_info_obj["right_share"] = dic["Right Share"]
        share_info_obj["right_share_value"] = dic["Right Share"].split("(")[0]
        share_info_obj["thirty_day_average_volume"] = float(str(dic["30-Day Avg Volume"]).replace(',', ''))
        share_info_obj["recorded_date"] = date.today()
        share_info_obj["share_symbol"] = ((response.url.split("="))[1]).upper()

        return share_info_obj

