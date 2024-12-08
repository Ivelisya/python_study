import requests
heads = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
}
url = 'https://passport.17k.com/ck/user/login'
data = {
    'loginName': '17346570232',
    'password': 'xlg17346570232'
}
session = requests.Session()
res = session.post(url,headers=heads,data=data)
print(res.text)