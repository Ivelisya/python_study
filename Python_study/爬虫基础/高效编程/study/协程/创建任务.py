import asyncio
async def run(i):
    print('我是开始')
    print('我是结束')
    
c = run(1)
# asyncio.run(c)
# 创建任务
task = asyncio.ensure_future(c)
# 开启循环
loop = asyncio.get_event_loop()
# 将任务放入循环
loop.run_until_complete(task) 
