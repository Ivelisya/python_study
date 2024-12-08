# 生成器是特殊的迭代器 集成了iter和next
# 函数将return改为yield生成生成器对象 使用next调用
# 装饰器可以给函数增添功能
# 装饰器也需要先定义
#outer是装饰器的名字
# def outer(f):
#     print(f)
# # f参数为被装饰函数的名字

def outer(f):
    def inner():
        print('登入功能')
        f()
    return inner

@outer
def func():
    print('注册功能')
    
func()