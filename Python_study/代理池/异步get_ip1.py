'''高效编程
协程异步 获取代理ip加端口

'''

import os
import asyncio
import aiohttp
import aiofiles
from lxml import etree
from aiohttp import ClientTimeout

# heads = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
#     'Cookie':'__51vcke__20L1wEeeGTFXijbh=90ac92be-ff5d-5eb7-a41b-52669e8d190c; __51vuft__20L1wEeeGTFXijbh=1695793347187; __root_domain_v=.zdaye.com; _qddaz=QD.649895793347593; acw_tc=781bad2516959148643014607e6b00529490741d261c5b9832df37b9dd8769; ASPSESSIONIDCUDDCSBC=GBMCLLMCMGFELPLJIPBODLJI; __vtins__20L1wEeeGTFXijbh=%7B%22sid%22%3A%20%22cad12791-586c-5492-86f0-76f578681d7c%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201695916692403%2C%20%22ct%22%3A%201695914892403%7D; __51uvsct__20L1wEeeGTFXijbh=2; Hm_lvt_dd5f60791e15b399bf200ae217689c2f=1695793348,1695914893; Hm_lpvt_dd5f60791e15b399bf200ae217689c2f=1695914893; _qdda=3-1.1; _qddab=3-na6e6u.ln3bxu66'
# }

def get_url():
    page = input('输入')
    url_list = []
    for n in range(int(page)):
        url = f'https://www.89ip.cn/index_{n}.html'
        url_list.append(url)
    return url_list

# for url in url_list:
#     res = requests.get(url,headers=heads)
#     html = res.content.decode()
#     # path = '代理池'
#     # with open(os.path.join(path,'ip.html'),'r',encoding='utf-8') as f:
#     #     html = f.read()
    tree = etree.HTML(html)
    ip = tree.xpath('//div[3]/div[1]/div/div[1]/table/tbody/tr/td[1]/text()|//div[3]/div[1]/div/div[1]/table/tbody/tr/td[2]/text()')
    ip_list = []
    for i in ip:
        ip_list.append(i.strip())
    for i in range(0,len(ip_list),2):
        print(ip_list[i] + ':' + ip_list[i+1])       
async def get_ip(url,heads):
    try:
        timeout = ClientTimeout(total=30)
        async with aiohttp.ClientSession(headers=heads,timeout=timeout) as session:
            async with session.get(url) as resp:
                html = await resp.text()
                tree = etree.HTML(html)
                ip = tree.xpath('//div[3]/div[1]/div/div[1]/table/tbody/tr/td[1]/text()|//div[3]/div[1]/div/div[1]/table/tbody/tr/td[2]/text()')
                ip_list = []
                path = '代理池'
                for i in ip:
                    ip_list.append(i.strip())
                for i in range(0,len(ip_list),2):
                    # print(ip_list[i] + ':' + ip_list[i+1])
                    async with aiofiles.open(os.path.join(path,'ip.txt'),'a',encoding='utf-8') as f:
                        await f.write(ip_list[i] + ':' + ip_list[i+1] + '\n')
                        print(ip_list[i] + ':' + ip_list[i+1] + '下载成功~')
    except:
        print('请求超时')              
async def main(url_list,heads):
    tasks = []
    for url in url_list:
        tasks.append(asyncio.create_task(get_ip(url,heads)))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    heads = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
    'Cookie':'__51vcke__20L1wEeeGTFXijbh=90ac92be-ff5d-5eb7-a41b-52669e8d190c; __51vuft__20L1wEeeGTFXijbh=1695793347187; __root_domain_v=.zdaye.com; _qddaz=QD.649895793347593; acw_tc=781bad2516959148643014607e6b00529490741d261c5b9832df37b9dd8769; ASPSESSIONIDCUDDCSBC=GBMCLLMCMGFELPLJIPBODLJI; __vtins__20L1wEeeGTFXijbh=%7B%22sid%22%3A%20%22cad12791-586c-5492-86f0-76f578681d7c%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201695916692403%2C%20%22ct%22%3A%201695914892403%7D; __51uvsct__20L1wEeeGTFXijbh=2; Hm_lvt_dd5f60791e15b399bf200ae217689c2f=1695793348,1695914893; Hm_lpvt_dd5f60791e15b399bf200ae217689c2f=1695914893; _qdda=3-1.1; _qddab=3-na6e6u.ln3bxu66'
}
    url_list = get_url()
    asyncio.run(main(url_list,heads))