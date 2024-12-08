from pymongo import MongoClient
# 连接mongodb
conn = MongoClient('localhost')
db = conn.smzy
data = db.mzy.insert_many([{'name':'smzy'},{'name':'张三'}])
print(data.inserted_ids)