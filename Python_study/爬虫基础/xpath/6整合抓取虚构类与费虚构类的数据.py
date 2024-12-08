from lxml import etree
import re
# 实例化
tree = etree.HTML(open('./素材/豆瓣.html', 'r', encoding='UTF-8').read())
'''
抓取封面
标题
简介
'''
li_list = tree.xpath('//ul[@class="cover-col-4 pl20 clearfix"]/li | //ul[@class="cover-col-4 clearfix"]/li')
for li in li_list:
    img = li.xpath('./a/img/@src')[0]
    title = li.xpath('./div/h2/a/text()')[0]
    info = li.xpath('./div/p[@class="color-gray"]/text() | ./div/p[@class="detail"]/text() | ./div/p[3]/text()')
    info = re.sub('\s', '', ''.join(info))
    print(img)
    print(title)
    print(info)
