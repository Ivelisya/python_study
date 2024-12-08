import asyncio
import time
async def run(url):
    print(f'向{url}抓取数据')
    # 挂起
    await asyncio.sleep(2)
    
async def main():
    task_list = []
    for i in range(3):
        c = run(i)
        task = asyncio.ensure_future(c)
        task_list.append(task)
    # 挂起耗时任务
    await asyncio.wait(task_list)
if __name__ == '__main__':
    start = time.time() 
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(time.time() - start)