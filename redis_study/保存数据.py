import redis
from lxml import etree
import requests
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
r = redis.StrictRedis(host='127.0.0.1',port=6379,password='123456',decode_responses=True)
url = 'https://www.dydytt.net/index.htm'
res = requests.get(url,headers=headers)
tree = etree.HTML(res.content.decode('GBK'))

