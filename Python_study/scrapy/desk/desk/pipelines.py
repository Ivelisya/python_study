# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline
class DeskPipeline:
    def process_item(self, item, spider):
        return item

class ImgPipeline(ImagesPipeline):
    # 1. 发送请求(下载图片, 文件, 视频,xxx)
    def get_media_requests(self, item, info):
        # 获取到图片的url
        url = item['img_src']
        # 进行请求
        yield scrapy.Request(url=url, meta={"url": url})  # 直接返回一个请求对象即可

    # 图片下载
    def file_path(self, request, response=None, info=None, *, item=None):
        # 当前获取请求的url的方式有2种
        # 获取到当前的url 用于处理下载图片的名称
        file_name = item['img_src'].split("/")[-1]  # 用item拿到url
        # file_name = request.meta['url'].split("/")[-1]  # 用meta传参获取

        # file_name也是scrapy的默认    return file_name是把下载的图片改成这个名字
        return file_name

    def item_completed(self, results, item, info):

        '''results是一个包含元组的列表,每个元组包含两个值
        第一个值表示处理结果的状态（成功或失败），
        第二个值包含了处理结果的详细信息'''
        # print('results', results)
        for r in results:
            # 获取每个图片的路径
            print(r[1]['path'])
        return item  # 一定要return item 把数据传递给下一个管道