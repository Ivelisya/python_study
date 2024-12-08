import re
import os
import aiohttp
import aiofiles
import asyncio
headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
                }
async def download_video(url,id,signal):
    while True:
        async with signal:
            try:
                async with aiohttp.ClientSession(headers=headers,timeout=60) as session:
                    print(url, '正在下载')
                    async with session.get(url, timeout=60) as resp:
                        res = await resp.read()
                        async with aiofiles.open (os.path.join('video',f'{id}') ,'w') as fp:
                            fp.write(res)
                            print('下载成功~')
                            break
            except:
                print(url,'下载失败~')
async def main():
    name_list = []
    url_list = []
    tasks = []
    with open('index.m3u8','r') as o:
        a = o.read()
            # re.search('https://hey03.cjkypo.com/20210807/sQa2Iywf/1200kb/hls/(.*?)#EXTINF:.*?',i)
        b = re.sub('\s','',a)
        c = b.split(',')
        # print(c)
        for i in c:
            try:
                name = re.search('https://hey03.cjkypo.com/20210807/sQa2Iywf/1200kb/hls/(.*?)#EXTINF:.*?',i).group(1)
                url = re.search('(.*?)#EXTINF:.*?',i).groups()[0]
                url_list.append(url)
                name_list.append(name)
            except AttributeError:
                pass
    if not os.path.exists('video'):
        os.makedirs('video')
    result = list(zip(url_list,name_list))
    signal = asyncio.Semaphore(100)
    for url,id in result:
        tasks.append(asyncio.ensure_future(download_video(url,id,signal)))
    await asyncio.wait(tasks)
    
if __name__ == '__main__':
    asyncio.run(main())