import re#用来匹配字符
# string = '我喜欢身高为170cm的女孩'
# result = re.findall('\d',string)#findall返回的是列表
# print(result)
# *任意多次 +至少一次 ？可有可无0,1 .除了换行的所有字符 （）分组 默认贪婪模式，尽可能多提取数据.*？表示非贪婪模式[]匹配集合中任意一个字符
# \d 匹配0到9数字


# string = 'https://www.baidu.com and http://www.baidu.com'
# ex = 'https?'
# result = re.findall(ex,string) re.search 
# print(result)
key = '你的手机号是1322292'
ex = '1[1-9]\d{5}'
result = re.findall(ex,key)
print(result)
# str.match 正则匹配
# AlgorithmExercises.match(/\d{11}/g) g为全局匹配 /replace正则替换 正则括号表示反锁
# .search查找




