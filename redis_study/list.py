import redis
r = redis.StrictRedis(password='123456',decode_responses=True)
# print(r.lpush('list',1,2,3))
# print(r.rpush('list',2,4,6))
# print(r.lrange('list',0,-1))
print(r.type('list'))