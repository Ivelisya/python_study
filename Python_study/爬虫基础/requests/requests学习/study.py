import requests
from lxml import etree
url = 'https://app.mi.com/'
heads={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"
}
response = requests.get(url=url,headers=heads)
with open('./2.html','wb') as fb:
    fb.write(response.content)
tree = etree.HTML(response.text)
list = tree.xpath('//div[@class="main index-page"]//li')
for i in list:
    app = i.xpath('./h5/a/text()')
    # print(etree.tostring(i,encoding ='utf-8').decode('utf-8'))