import requests
from bs4 import BeautifulSoup
url = ' http://httpbin.org/html'
try:
    response = requests.get(url,timeout=30)
    response.raise_for_status()
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text,"html.parser")
    h1_tag = soup.find("h1")
    if h1_tag:
        print(h1_tag.text.strip())
    else:
        print("没有h1_tag标签")

except:
    print("发生错误")