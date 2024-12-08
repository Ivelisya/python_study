import requests

url = 'https://so.gushiwen.cn/RandCode.ashx?'
res = requests.get(url)
with open('./yzm.jpg','wb') as fp:
    fp.write(res.content)   