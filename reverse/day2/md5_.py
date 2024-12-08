# from hashlib import md5
#
# md5()中的是盐,加盐防止撞库
# b前缀用于表示字节串（byte string）。当你在字符串（string）前面加上b，你告诉Python这是一个字节串而不是一个文本字符串
from hashlib import md5
def my_md5(a:str):
    obj = md5()
    data = a.encode("utf-8")
    obj.update(data)
    result = obj.hexdigest()
    print(result)
# update后接update计算出来是两次update的拼接
# 所以使用update
my_md5("123456")