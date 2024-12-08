import random
import time

import requests
from lxml import etree
from multiprocessing import Pool

def run(url,headers):
    # print(url, '正在抓取')
    
    res = requests.get(url, headers=headers)
    html = res.content.decode()
    # print(html)
    tree = etree.HTML(html)
    # 抓取每条数据
    div_list = tree.xpath('//div[@class="item"]')
    for div in div_list:
        # print(div)
        title = div.xpath('.//span[@class="title"]//text()')
        print(title)
    time.sleep(random.randint(1, 5))
    


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Cookie': 'bid=Xnvpbf2UbNg; __utmz=30149280.1662087122.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmz=223695111.1662087122.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __gads=ID=5028ab4b8008b53a-220b4cdd1ed600d1:T=1662087122:RT=1662087122:S=ALNI_MaI55OFkTI5OzNkCDeyUH-1zy45GA; ll="108288"; _vwo_uuid_v2=D3251E8A7AE16574645A511B7AEFFED12|aa508dc6a83b9857208dc21b35585366; __gpi=UID=000009611986ae99:T=1662087122:RT=1662343032:S=ALNI_MZVkkj-vdzxwX6USZE71UDU76THeA; __yadk_uid=DNXarKIhgDs7OOPwHlDaxNA2wcOjE4aX; gr_user_id=fd68f82d-ef5b-4795-af4d-659a761a5b01; ap_v=0,6.0; __utmc=30149280; __utmc=223695111; dbcl2="217661198:AoacdqjqELA"; ck=DvZ3; push_noty_num=0; push_doumail_num=0; frodotk_db="f3dfd9567fbe2376db9f8c037f3a6a62"; _pk_ses.100001.4cf6=*; __utma=30149280.1908426674.1662087122.1675258117.1675260664.9; __utmb=30149280.0.10.1675260664; __utma=223695111.1605720037.1662087122.1675258117.1675260664.9; __utmt=1; _pk_id.100001.4cf6=6a8c066053743026.1662087122.9.1675260807.1675258543.; __utmb=223695111.10.10.1675260664'
    }
    pool = Pool(3)
    # 同步抓取
    url = 'https://movie.douban.com/top250?start=0&filter='
    for i in range(0, 51, 25):
        url = f'https://movie.douban.com/top250?start={i}&filter='
        pool.apply_async(run, args=(url,headers))
    pool.close()
    pool.join()
    print('over')
