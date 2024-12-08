import requests
from lxml import etree
import re
import time
import threading
# from multiprocessing import Process
url = 'https://movie.douban.com/chart'
headers = {
        
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
        
}
start = time.time() 
def get_url():
    res = requests.get(url,headers=headers)
    text = res.content.decode()
    tree = etree.HTML(text)
    # //*[@id="content"]/div/div[1]/div/div/table[1]/tr/td[2]/div/a
    a = tree.xpath('//*[@id="content"]/div/div[1]/div/div/table/tr/td[2]/div/a/@href')
    return a

def get_movie_detail(detail_url):
    res = requests.get(detail_url,headers=headers)
    text = res.content.decode()
    tree = etree.HTML(text)
    tree.xpath('//*[@id="link-report-intra"]/span[1]/text()')
    # print(re.sub('\s','',''.join(detail)))
if __name__ == '__main__':
    url_list = get_url()
    lis = []
    for url in url_list:
        t = threading.Thread(target=get_movie_detail,args=(url,))
        # print(re.sub('\s','',''.join(get_movie_detail(url))))
        t.start()
        lis.append(t)
    for a in lis:
        a.join()
    print(time.time()-start)
    