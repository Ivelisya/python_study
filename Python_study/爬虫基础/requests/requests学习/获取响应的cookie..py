import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
}
url = 'https://xueqiu.com/'
res = requests.get(url,headers=headers)
# cookie = dict(res.cookies) #获取服务器端返回的cookie 并转换为字典 cookie值类型为字典
cookie = res.cookies #获取服务器端返回的cookie
res = requests.get('https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=535489&size=15',headers=headers,cookies=cookie)
print(res.content.decode())