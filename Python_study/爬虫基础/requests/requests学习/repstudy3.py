import requests
import json
# 1.对网站进行分析，定位到和地址栏url一样的数据包
# 2.response就是请求到的数据
# 3.再寻找其中有无想要的数据
# 搜索到了，说明可以直接发起请求获取你需要的数据
# 搜索不到，说明为动态加载数据 特指不是通过浏览器地址栏请求请求到的数据 动态加载数据一定是通过其他请求请求到的
# 如何获取动态加载数据 即通过ajax
# 基于抓包工具进行全局搜索 ctrl + f 搜索得到你想要的局部数据包 
# 在抓包工具中form data存放的是post请求的请求参数
# post请求中 处理请求参数的是data而不是params
url = 'https://movie.douban.com/j/chart/top_list?'
head = {
    "User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"
}
parms = {
    "type": "13",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "1"
}
response = requests.get(url = url,params = parms,headers=head)
page_text = response.json()
for dic in page_text:
    title = dic['title']
    print(title)
with open ('./1.json','w', encoding='utf-8') as fp:
    fp.write(response.text)

with open ('./1.json','r', encoding='utf-8') as op:
    data = json.load(op)
    print(data)