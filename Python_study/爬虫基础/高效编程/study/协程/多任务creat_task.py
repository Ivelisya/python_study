import asyncio
import time
start = time.time()
async def run(url):
    print('异步任务开始')
    await asyncio.sleep(3)
    print('异步任务完成')
    return url


def call_back(f):
    print('返回值为:',f.result())
    
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task_list = []
    for url in ['百度','阿里','京东']:
        coroutine = run(url)
        task = loop.create_task(coroutine)
        task.add_done_callback(call_back)
        task_list.append(task)
    loop.run_until_complete(asyncio.wait(task_list))
    print(time.time() - start)