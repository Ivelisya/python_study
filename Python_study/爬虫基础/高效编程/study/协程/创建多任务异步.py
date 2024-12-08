import asyncio
import time
async def run(url):
    print(f'向{url}抓取数据')
    # 挂起
    await asyncio.sleep(2)
start = time.time() 
# 开启了三个任务
for i in range(3):
    c = run(i)
    task_list = []
# print(time.time() - start)
    task = asyncio.ensure_future(c)
    task_list.append(task)
# 开启循环
loop = asyncio.get_event_loop()
# 将task_list转化成coroutine对象
loop.run_until_complete(asyncio.wait(task_list))
print(time.time() - start)