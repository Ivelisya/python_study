# requests模块的深入应用
# 正向代理隐藏真实ip  反向代理 隐藏了真实的服务器
# 使用代理 防止ip被封
# https://www.zdaye.com/free/
import requests
# proxies的形式：字典
proxies= [
    {'http':'http://117.50.175.254:7890'},
    {'http':'http://139.196.214.238:2087'}
  ]     
import random
proxy = random.choice(proxies)
proxy = random.choice(proxies)
result = requests.get("http://httpbin.org/ip", proxies=proxy)

print(result.text)