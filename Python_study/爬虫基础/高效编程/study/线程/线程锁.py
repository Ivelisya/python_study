import threading
# 创建锁
lock = threading.Lock()
# lock.acquire 上锁
# lock.release() 解锁
# with lock:简写，自动上锁，解锁