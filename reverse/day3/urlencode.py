'''
url的组成
协议://域名:端口/路径?查询字符串#锚点
url 统一资源定位符
为了防止url逻辑上的歧义，需要对url进行编码
会对中文和url里面的特殊符号进行处理
'''
# request会自动对url进行编码
# from urllib.parse import urlencode,quote,quote_plus
# s = 'https://www.simazhangyu.com/'
# # params = {
# #     'name': '张宇',
# #     'age': 18,
# #     'address': '北京'
# # }
# # p = urlencode(params)
# # print(p)
# # print(s + '?' + p)
# a = 'aaaadad213///'
# print(quote_plus(a))
from urllib.parse import urljoin
url = 'https://www.baidu.com/a/b'
u1 = '/c/d/index.html'
u2 = 'c/d/index.html'
print(urljoin(url,u1))
print(urljoin(url,u2))
