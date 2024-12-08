from multiprocessing.dummy import Pool#dummy虚拟的意思
import time
urls = ['www.1.com,www.2.com,www.3.com']
start = time.time()
def get_request(url):
    print('正在连接' ,url)
    time.sleep(2)
pool = Pool(5)
pool.map(get_request,urls)

print(time.time() - start)
pool.close()
