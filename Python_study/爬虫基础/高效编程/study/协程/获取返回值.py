import asyncio
async def run(i):
    print('我是开始'+ str(i))
    print('我是结束'+ str(i))
    await asyncio.sleep(3)
    return '返回值'
# 回调函数，获取返回值
def call_back(f):
    print(f.result())


c = run(1)
# asyncio.run(c)
# 创建任务
task = asyncio.ensure_future(c)
# 给任务添加回调
task.add_done_callback(call_back)
# 开启循环
loop = asyncio.get_event_loop()
# 将任务放入循环
loop.run_until_complete(task) 
