import 异步get_ip1
import 异步get_ip2
a = 异步get_ip2
b = 异步get_ip1
from proxy_redis import ProxyRedis
import os
# 实例化
p_r = ProxyRedis()
import re
heads = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
    'Cookie':'__51vcke__20L1wEeeGTFXijbh=90ac92be-ff5d-5eb7-a41b-52669e8d190c; __51vuft__20L1wEeeGTFXijbh=1695793347187; __root_domain_v=.zdaye.com; _qddaz=QD.649895793347593; acw_tc=781bad2516959148643014607e6b00529490741d261c5b9832df37b9dd8769; ASPSESSIONIDCUDDCSBC=GBMCLLMCMGFELPLJIPBODLJI; __vtins__20L1wEeeGTFXijbh=%7B%22sid%22%3A%20%22cad12791-586c-5492-86f0-76f578681d7c%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201695916692403%2C%20%22ct%22%3A%201695914892403%7D; __51uvsct__20L1wEeeGTFXijbh=2; Hm_lvt_dd5f60791e15b399bf200ae217689c2f=1695793348,1695914893; Hm_lpvt_dd5f60791e15b399bf200ae217689c2f=1695914893; _qdda=3-1.1; _qddab=3-na6e6u.ln3bxu66'
}
def get_ip():
    if not os.path.join('代理池','ip.txt'):
        url_list1 = a.get_url()
        url_list2 = b.get_url()
        a.asyncio.run(a.main(url_list1,heads))
        b.asyncio.run(b.main(url_list2,heads))
    with open(r'C:\Users\20212\smzy\代理池\ip.txt','r',encoding='utf-8') as f:
        ip = re.sub('\s',' ',f.read())
        old_ip_list = ip.split(' ')
        ip_list = [a for a in old_ip_list if a != '']
        for ip in ip_list:
            p_r.zset_zadd(ip)
get_ip()