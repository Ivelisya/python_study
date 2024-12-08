import requests
import os
import time
current_time = time.time()
url = 'https://www.spaceparty.cn/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"
}
response = requests.get(url, headers=headers)
html = response.content.decode()
if not os.path.exists('spaceparty.html'):
    with open('spaceparty.html', 'w', encoding='utf-8') as file:
        file.write(html)