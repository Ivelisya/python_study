import requests
from requests.exceptions import JSONDecodeError

headers = {
    "User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"
    
    
}
# url = https://www.iciba.com/
url =' https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_web_fanyi&sign=9cfdff94c4346abc'
data = {
'from':' en',
'to': 'zh',
'q': 'lucky'
    
}
res = requests.post(url = url,headers=headers,data = data)
print(res.status_code)
try:
    res_data = res. json()
except JSONDecodeError as e:
    print(f"解析JSON时发生错误： {e}")
    print("响应内容如下：")
    print(res.text)
print(res_data['content']['out'])