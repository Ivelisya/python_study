# beautifulsoup

## 一、beautifulsoup的简单使用

简单来说，Beautiful Soup是python的一个库，最主要的功能是从网页抓取数据。官方解释如下：

Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。
它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。

### 1、安装

```
pip install beautifulsoup4
```

pip install beautifulsoup4 -i http://pypi.douban.com/simple/

#### 1.1解析器

Beautiful Soup支持Python标准库中的HTML解析器,还支持一些第三方的解析器，如果我们不安装它，则 Python 会使用 Python默认的解析器，lxml 解析器更加强大，速度更快，推荐安装。

```python
pip install lxml
```

#### 1.2 解析器对比　

[官网文档](http://beautifulsoup.readthedocs.io/zh_CN/latest/)

### 2、快速开始

下面的一段HTML代码将作为例子被多次用到.这是 *爱丽丝梦游仙境的* 的一段内容(以后内容中简称为 *爱丽丝* 的文档):

```python
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
```

使用BeautifulSoup解析这段代码,能够得到一个 `BeautifulSoup` 的对象,并能按照标准的缩进格式的结构输出:

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'lxml')
# html进行美化
print(soup.prettify())
```

匹配代码

```python
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    Elsie
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link3">
    Tillie
   </a>
   
and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>
```

几个简单的浏览结构化数据的方法:

```python
soup.title  # 获取标签title
# <title>The Dormouse's story</title>

soup.title.name   # 获取标签名称
# 'title'

soup.title.string   # 获取标签title内的内容
# 'The Dormouse's story'

soup.title.parent  # 获取父级标签

soup.title.parent.name  # 获取父级标签名称
# 'head'

soup.p
# <p class="title"><b>The Dormouse's story</b></p>

soup.p['class']  # 获取p的class属性值
# 'title'

soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find(id="link3")  # 获取id为link3的标签
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
```

从文档中找到所有\<a>标签的链接:

```python
for link in soup.find_all('a'):
    print(link.get('href'))
    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie
```

从文档中获取所有文字内容:

```python
print(soup.get_text())
```

### 3、如何使用

将一段文档传入BeautifulSoup 的构造方法,就能得到一个文档的对象, 可以传入一段字符串或一个文件句柄.

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"))

soup = BeautifulSoup("<html>data</html>", 'lxml')
```

然后,Beautiful Soup选择最合适的解析器来解析这段文档,如果手动指定解析器那么Beautiful Soup会选择指定的解析器来解析文档。

## 二、beautifulsoup的遍历文档树

还拿”爱丽丝梦游仙境”的文档来做例子:

```python
html_doc = """
<html><head><title>The Dormouse's story</title></head>
    <body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
# lxml和html.parser解析的有时候会根据html是否完整而有解析不同的问题，需要注意
soup = BeautifulSoup(html_doc, 'html.parser')
```

通过这段例子来演示怎样从文档的一段内容找到另一段内容

### 1、子节点

一个Tag可能包含多个字符串或其它的Tag,这些都是这个Tag的子节点.Beautiful Soup提供了许多操作和遍历子节点的属性.

注意: Beautiful Soup中字符串节点不支持这些属性,因为字符串没有子节点。

#### 1.1 .contents

tag的 `.contents` 属性可以将tag的子节点以列表的方式输出:

```python
head_tag = soup.head
head_tag
# <head><title>The Dormouse's story</title></head>

head_tag.contents
[<title>The Dormouse's story</title>]

title_tag = head_tag.contents[0]
title_tag
# <title>The Dormouse's story</title>
title_tag.contents
# [u'The Dormouse's story']
```

字符串没有 `.contents` 属性,因为字符串没有子节点:

```python
text = title_tag.contents[0]
text.contents
# AttributeError: 'NavigableString' object has no attribute 'contents'
```



### 2、 节点内容

#### 2.1 .string

如果tag只有一个 `NavigableString` 类型子节点,那么这个tag可以使用 `.string` 得到子节点。如果一个tag仅有一个子节点,那么这个tag也可以使用 `.string` 方法,输出结果与当前唯一子节点的 `.string` 结果相同。

通俗点说就是：如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容。例如：

```python
print (soup.head.string)
#The Dormouse's story
# <title><b>The Dormouse's story</b></title>
print (soup.title.string)
#The Dormouse's story
```

如果tag包含了多个子节点,tag就无法确定，string 方法应该调用哪个子节点的内容, .string 的输出结果是 None

```python
print (soup.html.string)
#None
```

#### 2.2 .text

如果tag包含了多个子节点, text则会返回内部所有文本内容

```
print (soup.html.text)
```

**注意：**

strings和text都可以返回所有文本内容  

区别：text返回内容为字符串类型  strings为生成器generator

### 3、 **多个内容**

```
.strings .stripped_strings 属性
```

#### 3.1**.strings**

获取多个内容，不过需要遍历获取，比如下面的例子：

```python
for string in soup.strings:
    print(repr(string))
    
    
'''
  '\n'
"The Dormouse's story"
'\n'
'\n'
"The Dormouse's story"
'\n'
'Once upon a time there were three little sisters; and their names were\n'
'Elsie'
',\n'
'Lacie'
' and\n'
'Tillie'
';\nand they lived at the bottom of a well.'
'\n'
'...'
'\n'  
    
'''    
```

#### 3.2 **.stripped_strings** 

输出的字符串中可能包含了很多空格或空行,使用 `.stripped_strings` 可以去除多余空白内容

```python
for string in soup.stripped_strings:
    print(repr(string))


'''

"The Dormouse's story"
"The Dormouse's story"
'Once upon a time there were three little sisters; and their names were'
'Elsie'
','
'Lacie'
'and'
'Tillie'
';\nand they lived at the bottom of a well.'
'...'

'''
```

### 4、 父节点

继续分析文档树,每个tag或字符串都有父节点:被包含在某个tag中

#### 4.1 .parent

通过 `.parent` 属性来获取某个元素的父节点.在例子“爱丽丝”的文档中,\<head>标签是\<title>标签的父节点:

```python
title_tag = soup.title
title_tag
# <title>The Dormouse's story</title>
title_tag.parent
# <head><title>The Dormouse's story</title></head>
```

文档的顶层节点比如\<html>的父节点是 `BeautifulSoup` 对象:

```python
html_tag = soup.html
type(html_tag.parent)
# <class 'bs4.BeautifulSoup'>
```



## 三、beautifulsoup的搜索文档树

### 1、find_all

```python
find_all( name , attrs , recursive , string , **kwargs )
```

`find_all()` 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件:

```python
soup.find_all("title")
# [<title>The Dormouse's story</title>]

soup.find_all("a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find_all(id="link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

import re
# 模糊查询 包含sisters的就可以
soup.find(string=re.compile("sisters"))
# 'Once upon a time there were three little sisters; and their names were\n'
```

有几个方法很相似,还有几个方法是新的,参数中的 `string` 和 `id` 是什么含义? 为什么 `find_all("p", "title")` 返回的是CSS Class为”title”的\<p>标签? 我们来仔细看一下 `find_all()` 的参数.

#### 1.1 name 参数

`name` 参数可以查找所有名字为 `name` 的tag,字符串对象会被自动忽略掉.

简单的用法如下:

```python
soup.find_all("title")
# [<title>The Dormouse's story</title>]
```

搜索 `name` 参数的值可以使任一类型的 过滤器 ,字符串,正则表达式,列表,方法或是 `True` .

**<1> 传字符串**

最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容,下面的例子用于查找文档中所有的<b>标签

```python
soup.find_all('b')
# [<b>The Dormouse's story</b>]
```

**<2> 传正则表达式**

如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 `match()` 来匹配内容.下面例子中找出所有以b开头的标签,这表示\<body>和\<b>标签都应该被找到

```python
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
# body
# b
```

**<3> 传列表**

如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.下面代码找到文档中所有\<a>标签和\<b>标签

```python
soup.find_all(["a", "b"])
# [<b>The Dormouse's story</b>,
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```



#### 1.2 **keyword 参数**

如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,如果包含一个名字为 `id` 的参数,Beautiful Soup会搜索每个tag的”id”属性.

```python
soup.find_all(id='link2')
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

import re
# 超链接包含elsie标签
print(soup.find_all(href=re.compile("elsie")))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
# 以The作为开头的字符串
print(soup.find_all(text=re.compile("^The"))) 
# ["The Dormouse's story", "The Dormouse's story"]
# class选择器包含st的节点
print(soup.find_all(class_=re.compile("st")))
```

搜索指定名字的属性时可以使用的参数值包括 字符串 , 正则表达式 , 列表, True .

下面的例子在文档树中查找所有包含 `id` 属性的tag,无论 `id` 的值是什么:

```python
soup.find_all(id=True)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

使用多个指定名字的参数可以同时过滤tag的多个属性:

```python
soup.find_all(href=re.compile("elsie"), id='link1')
# [<a class="sister" href="http://example.com/elsie" id="link1">three</a>]
```

在这里我们想用 class 过滤，不过 class 是 python 的关键词，这怎么办？加个下划线就可以

```python
print(soup.find_all("a", class_="sister"))

'''
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
]

'''
```

通过 `find_all()` 方法的 `attrs` 参数定义一个字典参数来搜索包含特殊属性的tag:

```python
data_soup.find_all(attrs={"data-foo": "value"})
# [<div data-foo="value">foo!</div>]
```

注意：如何查看条件id和class同时存在时的写法

```python
print(soup.find_all('b', class_="story", id="x"))
print(soup.find_all('b', attrs={"class":"story", "id":"x"}))
```

#### 1.3  **text 参数**

通过 `text` 参数可以搜搜文档中的字符串内容.与 `name` 参数的可选值一样, `text` 参数接受 字符串 , 正则表达式 , 列表, True

```python
import re

print(soup.find_all(text="Elsie"))
# ['Elsie']

print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))
# ['Elsie', 'Lacie', 'Tillie']

# 只要包含Dormouse就可以
print(soup.find_all(text=re.compile("Dormouse")))
# ["The Dormouse's story", "The Dormouse's story"]
```

#### 1.4 **limit 参数**

`find_all()` 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用 `limit` 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 `limit` 的限制时,就停止搜索返回结果.

```python
print(soup.find_all("a",limit=2))
print(soup.find_all("a")[0:2])

'''
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, 
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
'''
```

### 2、find()

```python
find( name , attrs , recursive , string , **kwargs )
```

`find_all()` 方法将返回文档中符合条件的所有tag,尽管有时候我们只想得到一个结果.比如文档中只有一个\<body>标签,那么使用 `find_all()` 方法来查找\<body>标签就不太合适, 使用 `find_all` 方法并设置 `limit=1` 参数不如直接使用 `find()` 方法.下面两行代码是等价的:

```python
soup.find_all('title', limit=1)
# [<title>The Dormouse's story</title>]

soup.find('title')
# <title>The Dormouse's story</title>
```

唯一的区别是 `find_all()` 方法的返回结果是值包含一个元素的列表,而 `find()` 方法直接返回结果.

`find_all()` 方法没有找到目标是返回空列表, `find()` 方法找不到目标时,返回 `None` .

```python
print(soup.find("nosuchtag"))
# None
```

`soup.head.title` 是 tag的名字 方法的简写.这个简写的原理就是多次调用当前tag的 `find()` 方法:

```python
soup.head.title
# <title>The Dormouse's story</title>

soup.find("head").find("title")
# <title>The Dormouse's story</title>
```



## 四、beautifulsoup的css选择器

我们在写 CSS 时，标签名不加任何修饰，类名前加点，id名前加 #，在这里我们也可以利用类似的方法来筛选元素，用到的方法是 **soup.select()，**返回类型是 **list**

### 1、通过标签名查找

```python
print(soup.select("title"))  #[<title>The Dormouse's story</title>]
print(soup.select("b"))      #[<b>The Dormouse's story</b>]
```

### 2、通过类名查找

```python
print(soup.select(".sister")) 

'''
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, 
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

'''
```

### 3、id名查找

```python
print(soup.select("#link1"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
```

### 4、组合查找

组合查找即和写 class 文件时，标签名与类名、id名进行的组合原理是一样的，例如查找 p 标签中，id 等于 link1的内容，二者需要用空格分开

```python
print(soup.select("p #link2"))

#[<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
```

直接子标签查找

```python
print(soup.select("p > #link2"))
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
```

查找既有class也有id选择器的标签

```
a_string = soup.select(".story#test")
```

查找有多个class选择器的标签

```
a_string = soup.select(".story.test")
```

查找有多个class选择器和一个id选择器的标签

```
a_string = soup.select(".story.test#book")
```

### 5、属性查找

查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到。

```python
print(soup.select("a[href='http://example.com/tillie']"))
#[<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

select 方法返回的结果都是列表形式，可以遍历形式输出，然后用 get_text() 方法来获取它的内容：

```python
for title in soup.select('a'):
    print (title.get_text())

'''
Elsie
Lacie
Tillie
'''
```



## 练习

#### 1、匹配三国演义中的回合 并写入html文本中

![image-20220610123612886](./BS4解析完整.assets/image-20220610123612886.png)

### 2、匹配天气信息 城市与温度

只要城市与气温

![image-20220610123825110](./BS4解析完整.assets/image-20220610123825110.png)

匹配后结果为

![image-20220610123845530](./BS4解析完整.assets/image-20220610123845530.png)



### 3、匹配广州二手房 房源信息

匹配红色框内的内容

![image-20220610124307970](./BS4解析完整.assets/image-20220610124307970.png)
