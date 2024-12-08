from bs4 import BeautifulSoup
# 文件读取 获取HTML代码
f = open('C:\\Users\\20212\\smzy\\爬虫\\beautifulsoup\\素材\\豆瓣.html', 'r', encoding='UTF-8')
data = f.read()
f.close()
# print(data)

# 使用bs4的俩种方式
# 方式一
# soup = BeautifulSoup(data, 'lxml')
# print(type(soup))   #  <class 'bs4.BeautifulSoup'>

# 方式二
soup = BeautifulSoup(open('C:\\Users\\20212\\smzy\\爬虫\\beautifulsoup\\素材\\豆瓣.html', 'r', encoding='UTF-8'), 'lxml')
print(type(soup))   #  <class 'bs4.BeautifulSoup'>
print(soup.title.parent)