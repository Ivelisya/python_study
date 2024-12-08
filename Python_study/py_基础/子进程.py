import multiprocessing

def print_numbers():
    for i in range(10):
        print(i)

# 创建子进程
p = multiprocessing.Process(target=print_numbers)

# 启动子进程
p.start()

# 等待子进程完成
p.join()
