import requests
# import multiprocessing
from multiprocessing import Pool
# import threading
# import  asyncio
# from concurrent.futures import ThreadPoolExecutor
# import time

def run(url,headers):
    res = requests.get(url=url,headers=headers)
    print(res)

if __name__ == '__main__':
    headers = {
        'Referer':'https://so.gushiwen.cn/user/login.aspx?',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
    }
    url = 'http://web6650.us11.epep.eu.org/'
    pool = Pool()
    for i in range(9999):
        # url = 'http://web6650.us11.epep.eu.org/'
        pool.apply_async(run,args=(url,headers))
    pool.close()
    pool.join()
    print('over')