# 君子协议 robots
# requests就是爬虫中基于网络请求的模块
import requests
# 指定url
# 发起响应
# 获取响应数据（获取爬虫的数据）
# 持久化https://ie.sogou.com/存储
url = 'https://ie.sogou.com/'
head = {
    "User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"
}
# 发起请求 在网址当中一定是get请求
# 发送请求对象  客户端可以将数据封装在请求对象当中 获取响应数据
response = requests.get(url = url,headers=head)#url为get请求的第一个参数
# 将响应对象返回给response
# get请求 服务端返回一个响应对象 客户端从响应对象中获取索要数据
page_txt = response.text#txt返回字符串形式响应数据
with open('sougo.html','w',encoding = 'utf - 8') as fp:
    fp.write(page_txt)
print('数据爬取成功')
    