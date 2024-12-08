import pymysql
db = pymysql.connect(host = '127.0.0.1',port = 3306,user = 'root',password = '123456',database = 'smzy')
db.set_charset('utf8')
cursor = db.cursor()
sql = 'select * from user'
cursor.execute(sql)
print(cursor.fetchone())


