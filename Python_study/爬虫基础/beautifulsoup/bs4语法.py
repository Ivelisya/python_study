from bs4 import BeautifulSoup
import re
f = open('D:\\smzy\\爬虫\\beautifulsoup\\素材\\豆瓣.html', 'r', encoding='UTF-8')
data = f.read()
f.close()
soup = BeautifulSoup(data,'lxml')
print(type(soup))
print(soup.div)
# 获取当前页面中的第一个div标签
print(soup.img)
# 对象点
print(soup.a)
print(soup.find('div')) #为soup.div的复杂写法
soup.标签是soup.find的简写
# attrs代表页面属性
# 获取当前对象标签有哪些属性
print(soup.div.attrs['id'])
print(soup.div['id'])
soup_title = soup.title
ex = '<title>.*?</title>'
print(soup.title.string)
print(soup.get_text())
print(soup.title.text)
# string,get_text,text都是获取文本
soup_data = re.search(ex,soup_title.string)
print(soup_data.group(1))
re.search()
print(soup.title)
# repr原样输出
print(repr(soup.div.text))
print(repr(soup.div.string))
print(repr(soup.div.get_text()))
# 多重嵌套text,get_text(),单文本strign
# get_text = text
print(soup.find('div',attrs={
    'class':'global-nav'
}))
print(soup.find('div',class_ = "nav"))
# 找到div中第一个class属性的值
# attrs返回包含所有属性的字典
print(soup.find('a',class_ = 'cover').find('img')['src'])
print(soup.find('a',class_ = 'cover').find('img').attrs['src'])
print(soup.find('a',class_ = 'cover').img['src'])
print(type(soup.find('a',class_ = 'cover').img))
print(repr(soup.find('p',class_ = 'color-gray')))
data = repr(soup.find('p',class_ = 'color-gray'))
print(re.sub('\s','',data))
print(repr(soup.div.strings)) # 等同于text和get_text()返回的是生成器
print(repr(soup.div.stripped_strings)) # 返回的是生成器 去除空白符
print(repr(soup.div.text)) # 等同于get_text()
print(type(data))
# 获取所有封面超链接
print(soup.find_all('a',class_ = 'cover'))
print(soup.find('a',class_ = 'cover'))
print(soup.find_all('img')[0:2])
print(soup.find_all('img',limit=2))#只获取两个
# select选择器 返回列表
print(soup.select('div[class="nav-logo"]>a'))
print(soup.get_text())
# print(repr(next(soup.div.stripped_strings)))
# 配合正则使用
print(soup.find(text = re.compile('离开')))
# re.compile表示正则对象
# findall返回列表
for i in soup.find_all('img'):
    print(i['src'])
print(soup.find('a',class_ = 'cover').img['src'])#.attrs['src'])