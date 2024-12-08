import os.path

import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
def get_detail_href(url):
    res = requests.get(url, headers=headers)
    res.encoding = 'UTF-8'
    # print(res.text)
    soup = BeautifulSoup(res.text, 'html.parser')
    div_list = soup.find_all('div', attrs={'class': 'mulu-list quanji'})
    # print(div_list)
    book_href = []
    for d in div_list:
        a_list = d.find_all('a')
        # print(a_list)
        for a in a_list:
            book_href.append(a['href'])  # 获取所有的详情页href连接
    return book_href

def down_load_detail(url):
    # 获取书号以及书的卷名称
    book_number = url.split('/')[-1].split('.')[0]  # 获取章节号
    book_chapter_name = url.split('/')[-2]  # 获取url中卷名称
    res = requests.get(url, headers=headers)  # 抓取章节页内容
    res.encoding = 'UTF-8'
    # print(res.text)
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.find('h1').text.replace(':','').strip()  # 获取章节名称
    content = soup.find('div', class_='neirong', id='neirong').text  # 获取章节内容
    # 写入文件目录 判断不存在则创建章节目录
    path = f'{book_name}/{book_chapter_name}'
    if not os.path.exists(path):
        os.makedirs(path)
    # 写入文件中 文件名为章节名
    with open(os.path.join(path, book_number+'_'+title+'.txt'), 'w', encoding='UTF-8') as f:
        f.write(content)




if __name__ == '__main__':
    url = 'https://www.51shucheng.net/daomu/guichuideng'
    # book_list = get_detail_href(url)  # 获取当前所有章节的url
    # print(book_list)
    book_name = '鬼吹灯'
    # 判断当前书的文件夹是否存在 不存在则创建
    if not os.path.exists(book_name):
        os.mkdir(book_name)
    down_load_detail('https://www.51shucheng.net/daomu/guichuideng/fuxiandugu/3013.html')