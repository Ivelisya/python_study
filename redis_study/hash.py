import redis

r = redis.StrictRedis(host='127.0.0.1',port=6379,password='123456',decode_responses=True)
print(r.hset('hash','name','smzy'))
print(r.hgetall('hash'))
# print(r.hmset('myhash',{'name'}))
# print(r.hkeys())
print(r.hvals('hash'))