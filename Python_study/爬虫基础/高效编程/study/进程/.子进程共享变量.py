from multiprocessing import Process

# 进程之间内存独占
name = 'lucky'
def run():
    global name
    print(name)  # lucky
    name = '张三'
    print(name)  # 张三
# 在Python的multiprocessing模块中，每个进程都有其自己的命名空间，
# 即使它们的名字相同，也不会产生冲突。每个进程都有自己的内存空间，所以它们的变量名可以相同，但是这些变量在不同的进程中是互不影响的。


if __name__ == '__main__':
    p = Process(target=run)
    p.start()
    p.join()
    print(name)
    print('over')