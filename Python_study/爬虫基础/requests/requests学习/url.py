# 除了requests模块可以发送请求之外, urllib模块也可以实现请求的发送,只是操作方法略有不同!
import urllib.request

# 创建一个Request对象
response = urllib.request.Request("https://www.baidu.com")

# 使用urlopen方法发送请求并获取响应
response = urllib.request.urlopen(response)

# 打印请求的URL
print(response.geturl())

url = 'https://cn.bing.com/search?pglt=673&q=%E4%BD%A0%E5%A5%BD&cvid=2831f000aed64ddf8fc417a854c7efaa&aqs=edge..69i57j0l8.1073j0j1&FORM=ANNTA1&PC=LCTS'

print(urllib.request.unquote(url))
