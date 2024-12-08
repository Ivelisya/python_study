# import scrapy
# from selenium import webdriver
# from selenium.webdriver import Chrome
# from selenium.webdriver import ChromeOptions 
# from selenium.webdriver.chrome.options import Options
# class WySpider(scrapy.Spider):
#       name = 'wy'
#       # allowed_domains = ['news.163.com']
#       start_urls = ['https://news.163.com/domestic/']
#       # li_index = [1, 2, 4, 5]  # 当前要爬取菜单的索引位置
#       li_index = [1, 2]  # 当前要爬取菜单的索引位置
#       page_url = []
#       # 隐藏浏览器界面
#       chrome_option = Options()
#       chrome_option.add_argument('--headless')
#       chrome_option.add_argument('--disable-gpu')
#       option = ChromeOptions()
#       # 防止检测
#       option.add_experimental_option('excludeSwitches', ['enable-automation'])
#       # 导入配置
#       driver = webdriver.Chrome(options=chrome_option)
#       def parse(self, response, **kwargs):
#           # 抓取 国内 国际 军事 航空
#           menu = response.xpath('/html/body/div/div[3]/div[2]/div[2]/div/ul/li/a/@href').extract()
#           # 循环获取当前我们要抓取栏目的url
#           for i in range(len(menu)):
#               if i in self.li_index:
#                   url = menu[i]
#                   self.page_url.append(url)
#                   # 向详情页发起请求
#                   yield scrapy.Request(url, callback=self.parse_detail)
#       def parse(self, response):
#         # 抓取国内，国际板块的内容
#         # 返回了所有板块的url
#         url_list = response.xpath('/html/body/div/div[3]/div[2]/div[2]/div/ul/li/a/@href')[1:3].extract()
#         # print(url_list)
#         for i in range(len(url_list)):
#             if i in self.li_index:
#                 url = url_list[i]
#                 self.page_url.append(url)
#                 yield scrapy.Request(url,callback=self.parse_content)

#       def parse_content(self,response):
#             detail_url = response.xpath('/html/body/div/div[3]/div[3]/div[1]/div[1]/div/ul/li/div/a/@href').extract()
#             for url in detail_url:
#                 yield scrapy.Request(detail_url,callback=self.parse_detail)         
#       def parse_detail(self,response):
#           print(response)
# import scrapy
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# class WySpider(scrapy.Spider):
#     name = 'wy'
#     start_urls = ['https://news.163.com/domestic/']
#     li_index = [1, 2]  # Currently selected menu indexes
#     page_url = []

#     def __init__(self, **kwargs):
#         chrome_options = Options()
#         chrome_options.add_argument('--headless')
#         chrome_options.add_argument('--disable-gpu')
#         chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
#         self.driver = webdriver.Chrome(options=chrome_options)
#         super().__init__(**kwargs)

#     def parse(self, response):
#         url_list = response.xpath('/html/body/div/div[3]/div[2]/div[2]/div/ul/li/a/@href')[1:3].extract()
#         for i in range(len(url_list)):
#             if i in self.li_index:
#                 url = url_list[i]
#                 self.page_url.append(url)
#                 yield scrapy.Request(url, callback=self.parse_content)

#     def parse_content(self, response):
#         detail_url = response.xpath('/html/body/div/div[3]/div[3]/div[1]/div[1]/div/ul/li/div/a/@href').extract()
#         for url in detail_url:
#             yield scrapy.Request(url, callback=self.parse_detail)         

#     def parse_detail(self, response):
#         print(response)
from wangyi.items import WangyiItem
import scrapy
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options


class WySpider(scrapy.Spider):
    name = 'wy'
    # allowed_domains = ['news.163.com/domestic/']
    start_urls = ['http://news.163.com/domestic/']
    li_index = [1, 2]  # 索引为1 和2的url为国内和国际板块的url
    page_url = []  # 里面存放的为板块的url
    # 隐藏浏览器界面
    chrome_option = Options()
    chrome_option.add_argument('--headless')
    chrome_option.add_argument('--disable-gpu')
    # 防止检测
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 导入配置
    driver = Chrome(chrome_options=chrome_option, options=option)


    def parse(self, response, **kwargs):
        # 抓取国内和国际板块的数据
        # 返回了所有的板块的url
        url_list = response.xpath('/html/body/div/div[3]/div[2]/div[2]/div/ul/li/a/@href').extract()
        # print(url_list)
        for i in range(len(url_list)):
            if i in self.li_index:
                url = url_list[i]
                # 把板块对应的url存放起来
                self.page_url.append(url)
                yield scrapy.Request(url, callback=self.parse_detail)

    # 对于板块请求后的处理
    def parse_detail(self, response):
        # 抓取所有新闻对应详情页的url
        item = WangyiItem()
        url_list = response.xpath('/html/body/div/div[3]/div[3]/div[1]/div[1]/div/ul/li/div/div/a/@href').extract()
        for url in url_list:
            item['url'] = url
        print(item)
        yield item
