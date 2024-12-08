import threading

def print_numbers():
    for i in range(10):
        print(i)

# 创建子线程
t = threading.Thread(target=print_numbers)

# 启动子线程
t.start()

# 等待子线程完成
t.join()