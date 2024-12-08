import urllib.request
# from urllib import request
img_src = 'https://tse1-mm.cn.bing.net/th/id/OIP-C.Zte3ljd4g6kqrWWyg-8fhAHaEo?w=285&h=180&c=7&r=0&o=5&dpr=2&pid=1.7'
# urlretrieve 直接对图片发起请求，并将图片持久化保存
urllib.request.urlretrieve(img_src,'./123.jpg')