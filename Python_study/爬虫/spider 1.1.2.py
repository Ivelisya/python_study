import pymysql
import requests
from lxml import etree
import os
import re
from bs4 import BeautifulSoup
import aiohttp
import asyncio
import time


async def get_html(url):
    '''
    获取网页内容
    :param url: 网页链接
    :return: 网页内容
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url, headers=headers) as response:
            html = await response.text()
    return html


async def save_html(html):
    '''保存html到文件中'''
    if not os.path.exists('../1.html'):
        with open('../1.html', 'w', encoding='utf-8') as file:
            file.write(html)


async def read_html():
    with open('../1.html', 'r', encoding='utf-8') as file:
        html = file.read()
    return html


async def get_urls(html):
    '''获取所有的链接'''
    soup = BeautifulSoup(html, 'lxml')
    messy_list = soup.find_all('a', attrs={'class': 'post-title'})
    urls = []
    for i in messy_list:
        match = re.search(r'href="(.*?)"', str(i))
        if match:
            url = match.group(1)
            urls.append(url)
    return urls


async def get_content(index, url):
    '''获取网页内容'''
    content = await get_html(url)
    if not os.path.exists(f'{index}.html'):
        with open(f'{index}.html', 'w', encoding='utf-8') as file:
            file.write(content)
    tree = etree.HTML(content)
    title = str(tree.xpath('//h1[@class="entry-title"]/text()')[0])
    article = tree.xpath('//div[@class="entry-content"]//text()')
    return title, article


async def save_mysql(title, article):
    '''保存到mysql数据库中'''
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='123456',
        database='smzy',
        charset='utf8mb4'
    )
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO articles (title, content) VALUES (%s, %s)"
            cursor.execute(sql, (title, ''.join(article)))
            connection.commit()
    finally:
        connection.close()


async def main():
    current_time = time.time()
    url = 'https://simazhangyu.com'
    html = await get_html(url)
    await save_html(html)
    html = await read_html()
    urls = await get_urls(html)
    tasks = []
    for index, url in enumerate(urls):
        task = asyncio.create_task(get_content(index, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    for title, article in results:
        await save_mysql(title, article)
    print(time.time() - current_time)


if __name__ == '__main__':
    asyncio.run(main())