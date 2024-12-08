from typing import Iterable
import scrapy
from scrapy.http import Request


class DlSpider(scrapy.Spider):
    name = "dl"
    # allowed_domains = ["www.17k.com"]
    start_urls = ["https://user.17k.com/ck/user/myInfo/96139098?appKey=2406394919"]
    # cookie = 'GUID=80747f5d-a689-4552-90c3-1b7061fd799d; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F18%252F98%252F90%252F96139098.jpg-88x88%253Fv%253D1650527904000%26id%3D96139098%26nickname%3D%25E4%25B9%25A6%25E5%258F%258BqYx51ZhI1%26e%3D1712629641%26s%3Df880d38740c7322c; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2296139098%22%2C%22%24device_id%22%3A%2218b1f6e3519734-03efaa8be28a39-26031e51-1296000-18b1f6e351ae02%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2280747f5d-a689-4552-90c3-1b7061fd799d%22%7D; Hm_lvt_9793f42b498361373512340937deb2a0=1697039398,1697072905,1697118848; Hm_lpvt_9793f42b498361373512340937deb2a0=1697118857'
    # k_v = cookie.split(';')
    # cookie_dict = {i.split('=')[0].strip():i.split('=')[1] for i in cookie.split(';')}
    # for i in k_v:
    #     l = i.split('=')
    #     cookie_dict[l[0].strip()] = l[1].strip()
    def start_requests(self):
        cookie = 'GUID=80747f5d-a689-4552-90c3-1b7061fd799d; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F18%252F98%252F90%252F96139098.jpg-88x88%253Fv%253D1650527904000%26id%3D96139098%26nickname%3D%25E4%25B9%25A6%25E5%258F%258BqYx51ZhI1%26e%3D1712629641%26s%3Df880d38740c7322c; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2296139098%22%2C%22%24device_id%22%3A%2218b1f6e3519734-03efaa8be28a39-26031e51-1296000-18b1f6e351ae02%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2280747f5d-a689-4552-90c3-1b7061fd799d%22%7D; Hm_lvt_9793f42b498361373512340937deb2a0=1697039398,1697072905,1697118848; Hm_lpvt_9793f42b498361373512340937deb2a0=1697119250'
        cookie_dict = {i.split('=')[0].strip(): i.split('=')[1].strip() for i in cookie.split(';')}
        for url in self.start_urls:
            yield scrapy.Request(url,cookies=cookie_dict)

        
    def parse(self, response):
        print(response.text)