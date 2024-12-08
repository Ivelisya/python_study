import asyncio
import aiohttp
from proxy_redis import ProxyRedis
async def test_ip(ip,p_r):
    try:
        # 信号量并发控制
        async with aiohttp.ClientSession() as session:
            async with session.get('http://httpbin.org/ip',proxy = 'http://'+ip,timeout = 10) as resp:
                con = await resp.text()
                if con:
                        # 重新加入，设置成最大值
                    p_r.zset_zadd(ip)
                    print(ip + '访问成功')
                else:
                        # 降低权重  
                    p_r.zset.zincrby(ip)
    except:
        p_r.zset_zincrby(ip)  
        print(ip + '降低权重')  
    
async def main():
    p_r = ProxyRedis()
    ip_list = p_r.zset_zrange()
    # sem = asyncio.Semaphore(100)
    # print(ip_list)
    if ip_list:
        tasks = []
        for ip in ip_list:
            # 添加任务
            tasks.append(asyncio.create_task(test_ip(ip,p_r)))
        await asyncio.wait(tasks)
    
count = 0  
def run():
    global count
    while count < 5:
        asyncio.run(main())
        count += 1
run()