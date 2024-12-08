# ？后的内容代表请求参数
# 请求参数就是客户端发送给服务端的数据  多个请求参数使用&分割
# 分析网站反爬机制
# 伪装头信息 伪装请求载体的身份标识 (ua)伪装
# 最常见最通用的反爬机制，绝大多数网站都会携带这种反爬机制
import requests
# 参数动态化
head = {
    "User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"
}
keyword = input("请输入")
pram = {
    'query': keyword
}

url = 'https://www.sogou.com/web?'
response = requests.get(url=url, params=pram,headers=head)
FileName = keyword + ".html"
with open(FileName, 'wb') as fp:
    fp.write(response.content)