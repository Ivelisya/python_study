import asyncio
import time
def run(url):
    print(f'向{url}抓取数据')
    time.sleep(2)
start = time.time() 
for i in range(3):
    run(i)
print(time.time() - start)
    