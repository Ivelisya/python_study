from multiprocessing import Process
import time
start = time.time()
def run():
    print(1)
    time.sleep(1)
    
if __name__ == '__main__':
    j = []
    for i in range(5):
        p1 = Process(target = run)
        p1.start()
        j.append(p1)
    for i in j:
        i.join()
    print(time.time() - start)