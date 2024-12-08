from pymongo import MongoClient
# 连接mongodb
conn = MongoClient('localhost')
db = conn.test
data = db.smzy.insert_many([{'name':'smzy'},{'name':'张三'}])
print(data.inserted_ids)