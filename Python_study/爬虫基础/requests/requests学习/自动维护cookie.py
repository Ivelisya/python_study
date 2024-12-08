import requests
heads = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
}
url = 'https://xueqiu.com/'
session = requests.Session()
# 创建session来自动维护cookie
session.get(url,headers=heads)
# session用来储存cookie
# session保存cookie，下一次请求会带上前一次的cookie
url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=535489&size=15'
res = session.get(url,headers=heads)
print(res.text)