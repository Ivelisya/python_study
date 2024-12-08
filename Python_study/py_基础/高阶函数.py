s1 = 'hello'
# Exception通用异常类
# 一个try只能监测一种形式异常，如果有多种异常，处理第一个出现的异常
# raise主动抛出错误
try:
    a = int(s1)
except ValueError:
    print('异常')