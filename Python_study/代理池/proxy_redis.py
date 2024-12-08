import redis
from settings import *
import random
class ProxyRedis:
    def __init__(self):
        self.r = redis.Redis(host = HOST,port = PORT,password=PASSWORD,db=DB,decode_responses=True)
    def zset_zadd(self,ip):
        self.r.zadd(ZSET_NAME,{ip:SCORE})
        
    # 降低权重
    def zset_zincrby(self,ip):
        # 先查出权重
        score = self.r.zscore(ZSET_NAME,ip)
        if score > MIN_SCORE:
            self.r.zincrby(ZSET_NAME,-50,ip)
        else:
            # 删除ip
            print('ip权重过低已被删除')
            self.r.zrem(ZSET_NAME,ip)
    def get_ip(self):
        ip = self.r.zrangebyscore(ZSET_NAME,SCORE,SCORE,0,-1)
        if ip:
            return random.choice(ip)
        else:
            ip = self.r.zrangebyscore(ZSET_NAME,80,SCORE,0,-1)
            if ip:
                return random.choice(ip)
            else:
                print("实在没有~")
    # 返回所有的ip 以供test_ip 进行测试
    def zset_zrange(self):
        return self.r.zrange(ZSET_NAME,0,-1)
    
        