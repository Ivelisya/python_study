from lxml import etree
# etree.prase()解析本地html文件
# etree.HTML()解析网络html字符串
parser = etree.HTMLParser(encoding='UTF-8')
tree = etree.parse('D:\\smzy\\爬虫\\xpath\\豆瓣.html',parser=parser)
tree = etree.HTML(open('/爬虫基础/xpath\\豆瓣.html', 'r', encoding='utf-8').read())#实例化，etree.HTML中只能传入字符串     bs4实例化均可导入文件
a_list = tree.xpath('/html/body/div/div/div//a/text()')#//a div下所有的a
# /text()'    按照路径层级 一层一层往下找
# print(a_list)
for a in a_list:
    print(a.text)#获取标签中的文本
    print(etree.tostring(a,encoding  ='utf-8').decode('utf-8'))#先编码后解码 将节点对象转换为字符串
    
tree = etree.HTML(open('D:\\smzy\\爬虫\\xpath\\豆瓣.html','r',encoding='utf-8').read())
a_list = tree.xpath('//a')#获取页面中所有的a，不管a在哪
for a in a_list:
    print(a)
    print(etree.tostring(a,encoding  ='utf-8').decode('utf-8'))
# xpath中匹配属性值 前面加@
# last()最后一个  last（）-1倒数第二个
# 获取前两个
# 也可以使用切片 然后.xpath('.//text().)转化为文本
# 获取第一个
li = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li')[0].xpath('.//text()')
# 获取最后一个
li = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li')[-1].xpath('.//text()')
text = li.xpath('.//text()')#根据上面li的节点对象继续向下匹配
li = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li//text()')[-1]#等于上面
# .代表从当前节点往下
# ./代表从当前节点一层一层往下找
# .//就是//的意思，从当前节点往下的全部
# 当前匹配为全局匹配，与li节点无关，因为没有从li节点往下匹配
text = li.xpath('//text()')#等同于下面
text = tree.xpath('//text()')#等同于下面
print(li)
# 属性值获取  @加上属性名1
img_list = tree.xpath('//a/@href')
print(img_list)
# 当前作为了解
# 查找标签具有当前整个属性的节点
# a_list = tree.xpath('//a[@id])
# list = tree.xpath(//@id) 获取所有id属性对应的值
# //*[@id='content'].....不管当前是什么标签，id为content的我就要
# 逻辑运算
# and
# li = tree.xpath('//ul[@class="cover-col-4 clearfix"and@id='ai']')
# or
# li = tree.xpath('//ul[@class="cover-col-4 clearfix"or@id='ai']

# xpath复制问题 浏览器会自动补充
# 1.分析源码中是否有这个路径 2.检查xpath是否写错