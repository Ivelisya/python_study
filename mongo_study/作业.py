from pymongo import MongoClient
conn = MongoClient('localhost')
db = conn.smzy
a = db.smzy.find({"sex":{"$gt":0}})
print(next(a))