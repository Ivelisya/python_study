from proxy_redis import ProxyRedis

p = ProxyRedis()
ip_list = p.zset_zrange()
print(ip_list)