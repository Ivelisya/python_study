import redis

r = redis.StrictRedis(host='127.0.0.1',port=6379,password='123456',decode_responses=True)

# 设置
# print(r.set('name','smzy'))
# print(r.get('name'))
print(r.mset({'name':1,'sex':1}))
print(r.mget('name','sex'))