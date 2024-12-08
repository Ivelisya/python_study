import aiohttp
import asyncio
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url = 'http://www.whmc.edu.cn/') as resp:
            print(resp.status)
            text = await resp.text()
            print(text)
#semaphore,控制并发 
# asyncio.semaphore
asyncio.run(main())    