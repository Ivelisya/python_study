import re
import requests
import os
from concurrent.futures import ThreadPoolExecutor, wait

def download_video(url,id):
    while True:
        try:
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
            }
            res = requests.get(url=url,headers=headers)
            with open (os.path.join('video',f'{id}') ,'wb') as fp:
                fp.write(res.content)
            print('下载成功~')
            break
        except:
            print(url,'下载失败~')
if __name__ =='__main__':
    name_list = []
    url_list = []
    with open('index.m3u8','r') as o:
        a = o.read()
            # re.search('https://hey03.cjkypo.com/20210807/sQa2Iywf/1200kb/hls/(.*?)#EXTINF:.*?',i)
        b = re.sub('\s','',a)
        c = b.split(',')
        # print(c)
        for i in c:
            try:
                name = re.search('https://hey03.cjkypo.com/20210807/sQa2Iywf/1200kb/hls/(.*?)#EXTINF:.*?',i).group(1)
                url = re.search('(.*?)#EXTINF:.*?',i).groups()[0]
                url_list.append(url)
                name_list.append(name)
            except AttributeError:
                pass
    if not os.path.exists('video'):
        os.makedirs('video')
    result = list(zip(url_list,name_list))
    pool = ThreadPoolExecutor()
    for url,id in result:
        pool.submit(download_video,url,id)