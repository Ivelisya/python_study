l = ['1']
def run():
    print(l)
    l.append('2')
    print(l)
print(l)
run()
print(l)
# append可以更改全局变量

a = 1
def run():
    # print(a)
    a = 2
    print(a)
print(a)
run()
# 修改全局变量需要先声明