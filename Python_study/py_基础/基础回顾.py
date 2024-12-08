lis = []
# append追加，往最后添加一个数据
s = '123'
# 字符串不可变，所有的操作都会产生一个新的字符串
s.replace
# 所以字符串操作要放在一个新变量里
ret = lis.append(s)
# return   NONE
# 列表可变，字符串不可变
# pop拿出并删除一个 默认从最后
# remove删除一个
# len 长度，列表中的元素个数
# for a in lis:
    # 只能拿到元素，所以需要使用range来代替，然后通过if来判断
# 字典取值也可以使用get，get不会报错，拿不到数据返回none
# 快速拿到所有的key dic.keys() 返回不是列表
# 快速所有values dic.values()
# gbk中国使用 big-5 日本使用 unicode万国码 编码是为了用于便于传输 utf-8 unicode变种
# 被编码的数据需要解码
# Bytes才是计算机里真正的数据类型，也是网络数据传输中唯一的数据格式，
# 什么Json，
# Xml这些格式的字符串最后想传输也都得转成Bytes的数据类型才能通过socket进行传输，
# 而Bytes的数据与字符串类型数据的转换就是编码与解码的转换，
# utf-8是编解码时指定的格式。