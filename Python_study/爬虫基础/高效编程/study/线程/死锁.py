import threading

lock = threading.Lock()
lock.acquire()
lock.acquire()
print('1')