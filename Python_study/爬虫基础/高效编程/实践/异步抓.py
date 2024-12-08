import time
import aiohttp
import asyncio
from lxml import etree
import time
url = 'https://movie.douban.com/chart'
headers = {
        
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
        
}
start = time.time()   
async def get_url():
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as resp:
            text = await resp.read()
            tree = etree.HTML(text)
    # //*[@id="content"]/div/div[1]/div/div/table[1]/tr/td[2]/div/a
            a = tree.xpath('//*[@id="content"]/div/div[1]/div/div/table/tr/td[2]/div/a/@href')
    return a

async def get_movie_detail(detail_url):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(detail_url) as resp:
            text =await resp.read()
            tree = etree.HTML(text)
            detail = tree.xpath('//*[@id="link-report-intra"]/span[1]/text()')
    return detail
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    url_list = loop.run_until_complete(get_url())
    tasks = [get_movie_detail(url)for url in url_list]
    loop.run_until_complete(asyncio.gather(*tasks))
    print(time.time()-start)