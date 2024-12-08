import asyncio
async def run():
    print('我是run函数')
    
    
coroutine = run()
# print(coroutine) 
asyncio.run(coroutine)
# asyncio.run运行协程对象