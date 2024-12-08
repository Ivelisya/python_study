import requests
from lxml import etree
import os
path = input("输入路径")
if not os.path.exists(path):
    os.makedirs(path)
headers = {
    
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
    
}
url = "https://www.shicimingju.com/bookmark/sidamingzhu.html"
res = requests.get(url,headers=headers)
html = res.content.decode()
# print(html)
tree = etree.HTML(html)
div_list = tree.xpath('.//div[@class="book-item"]')
i = 0
for div in div_list:
    fm = div.xpath('./a/@href')[0]
    print(fm)
    img = div.xpath('./a/img/@src')[0]
    response = requests.get(img,headers=headers)
    with open(f'./{path}/sdmz{i}.jpg', 'wb') as f:
        f.write(response.content)
    i += 1