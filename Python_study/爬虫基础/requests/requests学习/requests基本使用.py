import requests
url = 'https://www.baidu.com'
response = requests.get(url)
print(response)
print(response.status_code)
print(response.encoding)
print(response.url)
print(response.ok)
print(response.request.headers)
# 获取响应内容为bytes的类型
print(response.content)
# 解码 utf-8或者gbk
print(response.content.decode('utf-8'))