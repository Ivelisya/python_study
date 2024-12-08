import time
from multiprocessing import Process
import os
def run():
    print('子进程开启','当前进程编号',os.getpid(),'父进程',os.getppid())
    time.sleep(1000)
    
if __name__ == '__main__':
    p = Process(target=run)
    p.start()
    p.join()
    
    
