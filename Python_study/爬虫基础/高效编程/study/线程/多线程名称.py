import os
import threading
import time
def run():
    # os.system('notepad')
    print('线程',threading.current_thread().name)
    time.sleep(5)
    print('结束',threading.current_thread().name)
    
if __name__ == '__main__':
    T = []
    for i in range(5):
        t = threading.Thread(target=run)
        # t2 = threading.Thread(target=run)
        t.start()
        # t1.join()
        # t.join()
        T.append(t)
    for i in T:
        i.join()
    print('over')