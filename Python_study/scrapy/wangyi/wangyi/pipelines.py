# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class WangyiPipeline:
    def open_spider(self, item):
        self.f = open('duanzi.txt', 'w', encoding='UTF-8')
    # 实现对item数据的处理
    def process_item(self, item, spider):
        # 取出item对象中的数据
        self.f.write(item['url']+'\n')
        # self.f.write(item['con']+'\n')
        return item
    # 关闭爬虫的时候执行一次
    def close_spider(self, item):
        self.f.close()
