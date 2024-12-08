import threading
num = 0
def run1():
    global num
    lock.acquire()
    for i in range(100000):
        num += i
        num -= i
    lock.release()
    print('run1', num)

def run2():
    global num
    lock.acquire()
    for i in range(100000):
        num += i
        num -= i
    lock.release()
    print('run2', num)
if __name__ == '__main__':
    lock = threading.Lock()
    t1 = threading.Thread(target=run1)
    t2 = threading.Thread(target=run2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)