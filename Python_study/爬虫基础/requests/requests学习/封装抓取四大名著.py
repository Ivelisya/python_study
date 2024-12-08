import os.path
import random
import time

import requests
from lxml import etree


def get_html(url):
    '''
    根据url进行抓取 返回页面HTML内容的函数
    :param url: 要抓取的url地址
    :return: 处理后的tree对象
    '''
    res = requests.get(url, headers=headers)
    # 获取抓取到的HTML内容
    html = res.content.decode()
    tree = etree.HTML(html)
    return tree


def get_books(tree):
    '''
    抓取四大名著书的url和书名
    :param tree: tree对象
    :return: {'三国演义': 'www.sanguoyanyi.com.....'}
    '''

    a_list = tree.xpath('//div[@class="book-item"]/h3/a')
    book_dict = {}
    for a in a_list:
        book_name = a.xpath('./text()')[0]
        # 拼接完整的url地址
        book_url = 'https://www.shicimingju.com' + a.xpath('./@href')[0]
        book_dict[book_name] = book_url
    return book_dict


def book_mulu(tree):
    '''
    获取章节的名称和url地址
    :param tree: tree对象
    :return: {'第一章三打白骨精'： 'www.sandabaigujing.com'...}
    '''
    a_list = tree.xpath('//div[@class="book-mulu"]/ul/li/a')
    mulu_dict = {}
    for a in a_list:
        mulu_name = a.xpath('./text()')[0]
        # 拼接完整的url
        mulu_url = 'https://www.shicimingju.com' + a.xpath('./@href')[0]
        mulu_dict[mulu_name] = mulu_url
    return mulu_dict


def get_book_content(tree, mulu_name):
    '''
    抓取章节的内容
    :param tree:  实例化的tree对象
    :param mulu_name:  章节名称
    :return: {'章节名': '内容'}
    '''
    # 直接匹配我们的书的内容  并拼接为字符串
    con = ''.join(tree.xpath('//div[@class="card bookmark-list"]//text()'))
    con_dict = {mulu_name: con}
    return con_dict


def save_book(book_name, con_dict):
    # 创建当前书的文件
    if not os.path.exists(book_name):
        os.mkdir(book_name)
    # 将字典中的内容写入文件中
    for mulu_name, con in con_dict.items():
        with open(os.path.join(book_name, mulu_name) + '.txt', 'w', encoding='UTF-8') as f:
            f.write(con)

def main(url):
    # 循环获取四大名著书名和url
    for book_name,book_url in get_books(get_html(url)).items():
        # print(book_name, book_url)
        # 循环获取每本书中的章节和章节url地址
        for book_mulu_name,mulu_url in book_mulu(get_html(book_url)).items():
            # 循环抓取章节中的内容
            mulu_con = get_book_content(get_html(mulu_url), book_mulu_name)
            # print(mulu_con)
            # 进行保存
            save_book(book_name, mulu_con)
            # time.sleep(random.randint(1, 4))  # 给时间自省
            print(book_name, book_mulu_name, '下载成功~')


if __name__ == '__main__':
    url = 'https://www.shicimingju.com/bookmark/sidamingzhu.html'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    main(url)