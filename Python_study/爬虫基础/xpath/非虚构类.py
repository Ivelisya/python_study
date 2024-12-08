from lxml import etree
import re
tree = etree.HTML(open(r'爬虫基础\xpaxh\豆瓣.html','r',encoding = 'utf-8').read())
li_list = tree.xpath('//ul[@class="cover-col-4 pl20 clearfix"]/li ')
for i in li_list:
    info = i.xpath('./div/p[@class="detail"]/text() | ./div/p[3]/text()')
    info1 = re.sub('\s','',''.join(info))
    print(info1)