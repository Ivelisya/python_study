from typing import Any
import scrapy
from scrapy.http import Response
from urllib.parse import urljoin


class ImgSpider(scrapy.Spider):
    name = "img"
    # allowed_domains = ["desk.zol.com.cn"]
    start_urls = ["https://desk.zol.com.cn/"]

    def parse(self, response):
        href_list_old = response.xpath('//div[@class="wrapper top-main clearfix"]/div[1]/div/ul/li/a/@href').extract()
        # //*[@id="pic6b"]/a
        for href in href_list_old:
            # url = f'https://desk.zol.com.cn/ + {href}'
            # if href.find('exe') != -1:
            # url = urljoin('https://desk.zol.com.cn/',href)
            url = f'https://desk.zol.com.cn/{href}'
            # print(url)
            # 返回详情页的url
            yield scrapy.Request(url,callback=self.parse_detail)

    def parse_detail(self,response):
        # 
        url_list = response.xpath('//div[5]/dl/dd/a/@href').extract()[:-1]
        # print(url_list)
        for url in url_list:
            detail_url = urljoin('https://desk.zol.com.cn/',url)
            yield scrapy.Request(detail_url,callback=self.parse_max_img)
    # 最后
    def parse_max_img(self,response):
        url = response.xpath('//img[1]/@src')[0].extract()
        yield {'img_:src':url}
# item是指最后yield的字典


            
        
