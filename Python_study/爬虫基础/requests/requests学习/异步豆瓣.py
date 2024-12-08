import requests
import os
from requests.exceptions import JSONDecodeError
import time
import random
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'
heads = {
    'Referer':'https://movie.douban.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
'cookie':'ll="118258"; bid=qyayv8RM1Ac; _pk_id.100001.4cf6=cc63684783c6e269.1693367567.; __yadk_uid=PXAdVsG5JWutIgCTTi29GxJcjbj9sN6D; _vwo_uuid_v2=DA95661CCFC6541ABCC08F251BB8CE6FD|2fd47d2c23302ac8473d09e38fd46ee4; __utma=30149280.884018519.1693367567.1693385308.1693745418.5; __utmc=30149280; __utmz=30149280.1693745418.5.4.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmb=30149280.2.10.1693745418; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1693745471%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; __utma=223695111.1246281176.1693367567.1693385308.1693745471.5; __utmb=223695111.0.10.1693745471; __utmc=223695111; __utmz=223695111.1693745471.5.4.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0'
}
params = {
    'type': 'movie',
    'tag': '热门',
    'page_limit': 50,
    'page_start': 0    
}
path = 'text'
if not os.path.exists(path):
    os.makedirs(path)
res = requests.get(url=url,headers=heads)
# print(res.content.decode())
data_json = res.json()["subjects"]
try:
    data_json = res.json()["subjects"]
except JSONDecodeError as e:
    print(f"解析JSON时发生错误： {e}")
    print("响应内容如下：")
    print(res.text)
# print(data_json)
for i in data_json:
    try:
        title = i['title']
        with open(f'./{path}/title.txt', 'a', encoding='utf-8') as f:
            f.write(title + '\n')
    except:
        pass
    # time.sleep(random.randint(1,4))
