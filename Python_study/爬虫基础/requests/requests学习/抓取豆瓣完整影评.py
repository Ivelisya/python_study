import requests
from lxml import etree
import re
import time
import random
url = "https://movie.douban.com/review/best/"
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
        'Cookie':'ll="118258"; bid=qyayv8RM1Ac; _pk_id.100001.4cf6=cc63684783c6e269.1693367567.; __yadk_uid=PXAdVsG5JWutIgCTTi29GxJcjbj9sN6D; _vwo_uuid_v2=DA95661CCFC6541ABCC08F251BB8CE6FD|2fd47d2c23302ac8473d09e38fd46ee4; __utmc=30149280; __utmz=30149280.1693745418.5.4.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmc=223695111; __utmz=223695111.1693745471.5.4.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1693751834; Hm_lpvt_16a14f3002af32bf3a75dfe352478639=1693751845; dbcl2="274062242:vIDMFkbFHzA"; ck=gCKQ; push_noty_num=0; push_doumail_num=0; frodotk_db="15b2ddf7e207bed4411899e7a6173c7c"; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1693757683%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; __utma=30149280.884018519.1693367567.1693751829.1693757683.7; __utmb=30149280.0.10.1693757683; __utma=223695111.1246281176.1693367567.1693751829.1693757683.7;'
}
res = requests.get(url = url,headers=head)
html = res.content.decode()
tree = etree.HTML(html)
div_list = tree.xpath('.//div[@class="review-list chart "]/div')
for div in div_list:    
    print(re.sub('\s','',''.join(div.xpath('.//div[@class="short-content"]/text()'))))
    id = div.xpath('./@data-cid')[0]
    common_url = f'https://movie.douban.com/j/review/{id}/full'
    resc = requests.get(url = common_url,headers=head)
    print(resc.json())
    time.sleep(random.randint(1,5))
print(div_list)