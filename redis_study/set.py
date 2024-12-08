import redis
r = redis.StrictRedis(password='123456',decode_responses=True)
print(r.sadd('set1','a','b','c'))

print(r.smembers('set1'))




 
 
 
 
 