# 使用collections中的lterable判断是否为可迭代对象
# isinstance
# iter和next实现迭代器  iter创造迭代器 next访问迭代器下一个元素
lis = [1,2,3,4]
#迭代器
# 创建一个迭代器，需要迭代器生成一到十数的平方值
class MyIter():
    def __init__(self,n):
        self.n = n
        self.index = 1
        
    def __iter__(self):
        return self
    def __next__(self):
        if self.index > self.n:
            raise StopIteration
        value = self.index ** 2
        self.index += 1
        return value
it = MyIter(10)
for i in it:
    print(i)
    