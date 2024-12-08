# 字典推导式
# {key: value for key, value in iterable}
import os.path
import random
import time
# import re
import requests
from lxml import etree
# path = 'sdmz'
# if not os.path.exists(path):
#     os.makedirs(path)
# headers = {
    
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
    
# }
def save_book(book_name,con_dict):
    if not os.path.exists(book_name):
        os.makedirs(book_name)
    for mulu_name,con in con_dict.items():
        # 以写入模式打开一个名为mulu_name.txt的文件，该文件位于book_name目录下。如果该文件不存在，则会创建一个新的空文件
        #s.path.join()函数用于将book_name和mulu_name两个字符串连接成一个路径。'w'参数表示以写入模式打开文件
        with open(os.path.join(book_name,mulu_name) + '.txt','w',encoding='utf-8') as f:
            f.write(con)
def get_html(url):
    """param : 要抓取的url"""
    
    # url = "https://www.shicimingju.com/bookmark/sidamingzhu.html"
    res = requests.get(url,headers=headers)
    html = res.content.decode()
    return html
def get_books(html):
    tree = etree.HTML(html)
    a_list = tree.xpath('.//div[@class="book-item"]/h3/a')
    book_dict = {}
    for a in a_list:
        book_name = a.xpath('./text()')[0]
        book_url = 'https://www.shicimingju.com/' + a.xpath('./@href')[0]
        book_dict[book_name] = book_url
    return book_dict 
def book_mulu(html):
    tree = etree.HTML(html)
    mulu_dict = {}
    li_list = tree.xpath('.//div[@class="book-mulu"]/ul/li')
    for li in li_list:
        mulu_name = li.xpath('./a/text()')[0]
        mulu_url = 'https://www.shicimingju.com/' + li.xpath("./a/@href")[0]
        # print(li.xpath("./a/@href"),li.xpath('./a/text()'))
        mulu_dict[mulu_name] = mulu_url
    return mulu_dict
def get_book_content(a,mulu_name):
    tree = etree.HTML(a)
    con = ''.join(tree.xpath('.//div[@class="card bookmark-list"]//text()'))
    con_dict = {mulu_name:con}
    return con_dict

def main(url):
    for book_name,book_url in get_books(get_html(url)).items():
        for book_mulu_name,mulu_url in book_mulu(get_html(book_url)).items():
            mulu_con = get_book_content(get_html(mulu_url),book_mulu_name)
        # print(book_name,book_url)
            # print(mulu_con)
            # exit()
            save_book(book_name,mulu_con)
            time.sleep(random.randint(1,4))
if __name__ == '__main__':
    url = "https://www.shicimingju.com/bookmark/sidamingzhu.html"
    headers = {
    
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
    
}
    main(url)