"""
抓取封面
标题
简介    
    """
from lxml import etree
import re
parser = etree.HTMLParser(encoding='utf-8')
tree = etree.parse(r'爬虫基础\xpaxh\豆瓣.html', parser=parser)
li_list = tree.xpath('//ul[@class = "cover-col-4 clearfix"]/li')
for li in li_list:
    img = li.xpath('./a/img/@src')
    title = li.xpath('./div/h2/a/text()')
    info = li.xpath('./div/p[@class="color-gray"]/text() | ./div/p[@class="detail"]/text()')
    # info = li.xpath('./div/p[@class="color-gray"]/text() | ./div/p[@class="detail"]/text()')
    info1 = re.sub('\s','',''.join(info))
    print(info1)
    print(img)
    print(title)