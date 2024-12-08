import requests
head = {
    "User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"
}
img_src = 'https://tse1-mm.cn.bing.net/th/id/OIP-C.Zte3ljd4g6kqrWWyg-8fhAHaEo?w=285&h=180&c=7&r=0&o=5&dpr=2&pid=1.7'
response = requests.get(url = img_src,headers=head)#对图片发起请求
img_data = response.content#获取图片数据 采用二进制，因为多媒体资源一般采用二进制在网上传播
#持久化存储
with open('./background.jpg','wb') as fp:
    fp.write(img_data)