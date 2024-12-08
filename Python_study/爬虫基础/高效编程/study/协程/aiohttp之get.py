import aiohttp
import asyncio
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url = 'http://www.whmc.edu.cn/') as resp:
            print(resp.status)
            text = await resp.text()
            print(text)
            
            
asyncio.run(main())