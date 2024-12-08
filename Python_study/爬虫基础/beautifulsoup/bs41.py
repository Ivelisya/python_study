# 方式一
from bs4 import BeautifulSoup
f = open('C:\\Users\\20212\\smzy\\爬虫\\beautifulsoup\\素材\\豆瓣.html', 'r', encoding='UTF-8')
data = f.read()
f.close()
# soup = BeautifulSoup(data,'lxml')
# print(type(soup))
# soup实例化
# 方法二
soup = BeautifulSoup(open('./爬虫/beautifulsoup/素材/豆瓣.html','r',encoding='UTF-8'),'lxml')
print(type(soup))
# re.compile返回一个正则对象