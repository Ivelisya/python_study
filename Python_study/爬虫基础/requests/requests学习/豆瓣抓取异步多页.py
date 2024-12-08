import requests
from lxml import etree
import json
page = eval(input())
heads = {
   "Referer":"https://movie.douban.com/explore",
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
    'Cookie':'Cookie:ll="118258"; bid=qyayv8RM1Ac; __utmc=30149280; __utmz=30149280.1693745418.5.4.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=30149280.884018519.1693367567.1693745418.1693751829.6; __utmb=30149280.0.10.1693751829; dbcl2="274062242:vIDMFkbFHzA"; ck=gCKQ; push_noty_num=0; push_doumail_num=0; frodotk_db="15b2ddf7e207bed4411899e7a6173c7c"; ap_v=0,6.0'}
for i in range(0,(page-1)*20+1,20):
    url = f'https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start={(page-1)*20}&count=20&selected_categories=%7B%7D&uncollect=false&tags=&'
    res = requests.get(url=url,headers=heads)._content
    # print(res.content.decode())
    items = json.loads(res)['items']
    for title in items:
        try:
            t = title['title']
            print(t)
        except:
                pass
    
    # tree = etree.HTML(html)
    # div_list = tree('//ul[@class="explore-list"]/li')
    # for li in div_list:
    #     print(li)