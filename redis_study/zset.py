import redis
r = redis.StrictRedis(password='123456',decode_responses=True)
print(r.zadd('zadd',{'a':1,'b':2,'c':3}))
print(r.zcard('zadd'))
print(r.zscore('zadd','a'))
print(r.type('zadd'))
