from multiprocessing import Process
import time
start = time.time()
def run():
    time.sleep(1)
    
if __name__ == '__main__':
    # 创建子进程
    # p1 = Process(target = run)
    p2 = Process(target = run)
    # p1.start()
    # p2.start()
    # p1.join()
    p2.join()
    # 主进程等待子进程
    print(time.time() - start)