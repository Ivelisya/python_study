import requests
from lxml import etree
import os
import re
from bs4 import BeautifulSoup
url = 'http://8.130.9.29/'
head = {
    "User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"
}
response = requests.get(url,headers=head)
# print(response.text)
html = response.content.decode()
# print('网站html爬取成功')
# 判断目录下是否存在
if not os.path.exists('1.html'):
    with open('1.html', 'w', encoding='utf-8') as fp:
        fp.write(html)
with open('1.html', 'r', encoding='utf-8') as op:
    html = op.read()
    print('成功读取到html信息')
    tree = etree.HTML(html)
    post_content_list = tree.xpath('.//div[@class="post-content-wrap"]')
    # href = tree.xpath('//*[@id="main"]/articles[1]/div[2]/div/a/text()')
    # print(post_content)
    # 不规范html，lxml无法正常拿到url，使用bs4进行选取
    soup = BeautifulSoup(html, 'lxml')
    messy_list = soup.find_all('a', attrs={
        'class': 'post-title'
    })
    # 此处得到的mesyy_list并不是个列表，而是bs4对象
    print(type(messy_list))
    urls = []
    for i in messy_list:
        pattern = r'href="(.*?)"'
        print(type(i))
        match = re.search(pattern, str(i))
        if match:
            url = match.group(1)
            urls.append(url)
        # print(match)
    print(urls)
    for content in post_content_list:
        # article_time = content.xpath('.//div[@class="post-date"]//text()')[1]
    # print(article_time)
    # print(html)
    #     print(type(article_time))
    #     exit()
        article_time = re.sub('\s', '', content.xpath('.//div[@class="post-date"]//text()')[1])
        # article_content = re.sub('\s','',content.xpath())
        # href = content.xpath('div/a/text()')
        # print(href)
        # print(article_time)
        # print(re.sub('\s','',article_time))
for index, i in enumerate(urls):
    print(index)
    if index == 0:
        content = requests.get(i, headers=head).content.decode()
        if not os.path.exists(f'{index + 2}.html'):
            with open(f'{index + 2}.html','w',encoding='utf-8') as fp:
                fp.write(content)
        tree = etree.HTML(content)
        article1 = tree.xpath('//*[@id="post-35"]/div//text()')
        # 和bs4不同，此时为list列表
        new_article1 = [item for item in article1 if item.strip()]
        article = ','.join(new_article1)
        print(article)

    if index == 1:
        content = requests.get(i, headers=head).content.decode()
        if not os.path.exists(f'{index + 2}.html'):
            with open(f'{index + 2}.html', 'w', encoding='utf-8') as fp:
                fp.write(content)
        tree = etree.HTML(content)
        article2 = tree.xpath('//*[@id="post-28"]/div/p/text()')[0]
        # new_article2= [item for item in article2 if item.strip()]
        # articles = ','.join(new_article2)
        print(article2)



