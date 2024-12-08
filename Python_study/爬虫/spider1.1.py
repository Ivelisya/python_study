import pymysql
import requests
from lxml import etree
import os
import re
from bs4 import BeautifulSoup
import time
current_time = time.time()
url = 'http://simazhangyu.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"
}

# 发送请求，获取网页内容
response = requests.get(url, headers=headers)
html = response.content.decode()

# 保存网页内容到文件
if not os.path.exists('../1.html'):
    with open('../1.html', 'w', encoding='utf-8') as file:
        file.write(html)

# 读取保存的文件内容
with open('../1.html', 'r', encoding='utf-8') as file:
    html = file.read()

# 使用解析器解析网页内容
soup = BeautifulSoup(html, 'lxml')
messy_list = soup.find_all('a', attrs={'class': 'post-title'})
print(messy_list)
urls = []
for i in messy_list:
    match = re.search(r'href="(.*?)"', str(i))
    if match:
        url = match.group(1)
        urls.append(url)

# 连接MySQL数据库
connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    database='smzy',
    charset='utf8mb4'
)

try:
    with connection.cursor() as cursor:
        for index, url in enumerate(urls):
            response = requests.get(url, headers=headers)
            content = response.content.decode()
            if not os.path.exists(f'{index}.html'):
                with open(f'{index}.html', 'w', encoding='utf-8') as file:
                    file.write(content)
            tree = etree.HTML(content)
            # if index == 0:
            title = str(tree.xpath('//h1[@class="entry-title"]/text()')[0])
            article1 = tree.xpath('//div[@class="entry-content"]//text()')
            article = ','.join(item.strip() for item in article1 if item.strip())
            # print(articles)
            #     # 插入第一个文章内容到数据库
            sql = "INSERT INTO articles (title,content) VALUES (%s,%s)"
            cursor.execute(sql, (title,article))
            connection.commit()
            # if index == 1:
            #     articles = tree.xpath('//*[@id="post-28"]/div/p/text()')[0]
            #     # 插入第二个文章内容到数据库
            #     sql = "INSERT INTO articles (content) VALUES (%s)"
            #     cursor.execute(sql, (articles,))
            #     connection.commit()
finally:
    connection.close()
print(time.time() - current_time)