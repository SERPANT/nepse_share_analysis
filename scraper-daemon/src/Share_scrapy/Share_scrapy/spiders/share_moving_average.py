import scrapy

from Share_scrapy.constants.moving_average_links import MOVING_AVERAGE_LINKS

class ShareMovingAverageSpider(scrapy.Spider):
    name = 'share_moving_average'
    allowed_domains = ['www.sharesansar.com']
    start_urls = MOVING_AVERAGE_LINKS["CommercialBankShare"]

#     DEFAULT_REQUEST_HEADERS = {
#         Accept: application/json,
#         Accept-Encoding: gzip, deflate, br
#         Accept-Language: en-US,en;q=0.9
#         Connection: keep-alive
# Cookie: _ga=GA1.2.356551568.1619539379; __gads=ID=0757c0982a0bb0e8-22c8e049a1c700ad:T=1619539379:RT=1619539379:S=ALNI_MaEgN8u5mQ_nGJSwXhiyS-ObRporA; _gid=GA1.2.49043377.1622355817; XSRF-TOKEN=eyJpdiI6IlVoRm5DTDRGQk1sVmtseG5Ydm95OHc9PSIsInZhbHVlIjoidGNsbGtKbGRJMVpiRUExbU5yTW13aHhXOUFrblNVMkZuS0NuNVRPUDBJcXhCODNjWjdLSTVRRjN0OEJTd2N1dyIsIm1hYyI6ImZkYzU4YzI5OGFhNjg5NTIwNzMyYmY4NWY4MTAzY2E1NDAyMjEzYzdhMGM0NjcxNDA2MDE5ODljYTVhNjBmNGQifQ%3D%3D; sharesansar_session=eyJpdiI6IndtbnRzNEdtM05MXC9GYVp3UmZQcTdnPT0iLCJ2YWx1ZSI6Ilk2anM4SWtjSzZoWTVWcWxLc2hyTXJRTm5VMlBkbHV4UmxhSnIxeG80OGRVVWJYME1MVUNSZjZyYWwydkxkS2w3bm0rdDcyak1VOU1uZ1FDUEVjNFJPK2lEVFM0Q210STRxWXZCbGNsS1FZXC9XWXhuN1VvSEg2NHlXVmRTWHlwMSIsIm1hYyI6Ijk5MmEyNTZlZDg0ZmM0YjI4YmE2YjA2NWVjMDk1YzNiMmQ3NmRkMGEwY2U2ZGM0ODIwZGM3OGUwMDQ1NmZmZDcifQ%3D%3D
# Host: www.sharesansar.com
# Referer: https://www.sharesansar.com/company/nmb
# sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"
# sec-ch-ua-mobile: ?0
# Sec-Fetch-Dest: empty
# Sec-Fetch-Mode: cors
# Sec-Fetch-Site: same-origin
# X-Requested-With: XMLHttpRequest
#     }

    def parse(self, response):
        print("=---------------------------------------")
        print("=---------------------------------------")
        print("=---------------------------------------")
        print("=---------------------------------------")
        print("=---------------------------------------")
        data_rows = response.xpath("//*[@id='myTable']").getall()
        print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        print(data_rows)
        # for row in data_rows:
        #     print(row.get())
