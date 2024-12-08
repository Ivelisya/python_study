# import requests
# url = 'https://www.nmpa.gov.cn/hzhp/hzhpjgdt/index.html'
# head = {
#     "User-Agent":
# "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# }

# response = requests.get(url=url,headers=head)
# with open('1.html','wb') as fp:
#     fp.write(response.content)
import requests
from requests.exceptions import JSONDecodeError
# 指定url
url = 'https://piaofang.maoyan.com/dashboard-ajax?orderType=0&uuid=18a47152329c8-0369801b9d3167-7f5d547b-13c680-18a47152329c8&timeStamp=1693412051381&User-Agent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTYuMC4xOTM4LjYy&index=36&channelId=40009&sVersion=2&signKey=9deac80cdaeca4ad6ea39b3e6a853725'
parm = {
    "orderType": "0",
    "uuid": "18a47152329c8-0369801b9d3167-7f5d547b-13c680-18a47152329c8",
    "timeStamp": "169341221938",
    "User-Agent": "TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTYuMC4xOTM4LjYy",
    "index":" 190",
    "channelId": "40009",
    "sVersion":" 2",
    "signKey": "d2fdf707669036dda183b49872d44c9a"
}
# ua伪装
head = {
    "User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"
}
# 发起请求,并获取响应数据
data = requests.get(url = url,params = parm,headers=head)
my_dict = {}
# 错误捕获
try:
    data_json = data.json()
except JSONDecodeError as e:
    print(f"解析JSON时发生错误： {e}")
    print("响应内容如下：")
    print(data.text)
with open ('./1.txt','w', encoding='utf-8') as fp:
    for div in data_json['movieList']['data']['list']:
        Name = div["movieInfo"]["movieName"]
        releaseInfo = div["movieInfo"]['releaseInfo']
        showCount = div['showCount']
        fp.write(f'{Name}{releaseInfo}\n')
        my_dict[Name] = showCount
    print('程序运行正常')
# 对爬取到的数据排序
my_dic = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}
# k: v for k, v in sorted(my_dict.items(), key=lambda item: item[0])
# sorted(iterable, key=None, reverse=False)
# iterable 表示要排序的可迭代对象，可以是列表、元组、字符串等；key 是一个可选参数，用于指定一个函数，该函数将作用于每个元素上，并根据其返回值进行排序；
# reverse 也是一个可选参数，用于指定是否按照降序排序，默认为升序排序。
print(my_dic)
# 检查是否成功写入
with open ('./1.txt','r', encoding='utf-8') as op:
    data = op.read()
    print(data)

    