import requests
import re
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }
# res = requests.get('https://s1.zoubuting.com/20210807/sQa2Iywf/index.m3u8',headers=headers)
# print(res.content)
"""
https://s1.zoubuting.com/20210807/sQa2Iywf/index.m3u8
          
          /20210807/sQa2Iywf/1200kb/hls/index.m3u8
https://s1.zoubuting.com/20210807/sQa2Iywf/1200kb/hls/index.m3u8
"""
url = 'https://s1.zoubuting.com/20210807/sQa2Iywf/1200kb/hls/index.m3u8'
res = requests.get(url,headers=headers) 
with open('index.txt','wb') as fp:
    fp.write(res.content)