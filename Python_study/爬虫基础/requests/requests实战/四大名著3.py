import requests
from lxml import etree
import re
import time
start = time.time()
headers = {
    
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
    
}
page = eval(input())
for i in range(0,page+1):
    url = f"https://www.shicimingju.com/book/sanguoyany/{i}.html"
    res = requests.get(url,headers=headers,timeout=3)
    html = res.content.decode()
    tree = etree.HTML(html)
    con = tree.xpath('.//div[@class="card bookmark-list"]//text()')
    print(re.sub('\s','',''.join(con)))
print(time.time() - start)