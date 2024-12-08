from bs4 import BeautifulSoup
import re
with open('C:\\Users\\20212\\smzy\\爬虫\\beautifulsoup\\素材\\三国演义.html','r',encoding='UTF-8') as fp:
    soup = BeautifulSoup(fp,'lxml')
    soup_data = soup.select('div[class="book-mulu"]>ul>li>a')
    ex = '<a href="/book/sanguoyanyi/(.*?).html">(?P<name>.*?)</a>'
    with open('./1.txt','w',encoding='UTF-8') as fb:
        for i in soup_data:
            a = re.search(ex,str(i))
            # print(a.group('name'))
            b = a.group('name')
            # fb.write(i.string + '\n')
            fb.write(b + '\n')
with open('1.txt','r',encoding='utf-8') as ob:
    data = ob.read()
    print(data)