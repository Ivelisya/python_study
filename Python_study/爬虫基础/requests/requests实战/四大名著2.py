import requests
from lxml import etree
headers = {
    
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
    
}
url = "https://www.shicimingju.com/book/sanguoyanyi.html"
res = requests.get(url,headers=headers)
html = res.content.decode()
# print(html)
tree = etree.HTML(html)
li_list = tree.xpath('.//div[@class="book-mulu"]/ul/li')
for li in li_list:
    print(li.xpath("./a/@href"),li.xpath('./a/text()'))
