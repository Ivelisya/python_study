import asyncio
async def run():
    print('我是run函数')
    
# 创建一个协程对象 
coroutine = run()
# 新版本
# asyncio.run(coroutine) 中封装的是loop.run_until_complete
# 创建事件循环
loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
print(loop)
