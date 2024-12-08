import requests
import pymysql
from lxml import etree
db = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root',password='123456',database='smzy')
# print(db)
# 设置字符编码
db.set_charset('utf8')
# 创建游标对象
cursor = db.cursor()
# 执行sql语句
# sql = 'insert into user values(4,"lucky" ,1,1)'
# cursor.execute(sql)
# print(cursor.fetchall())
# print(cursor.fetchone())
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }
url = 'https://www.3dcax.com/'
res = requests.get(url,headers=headers)
data = res.content.decode()
# print(data)
tree = etree.HTML(data)
a_list = tree.xpath('/html/body/main/div/div[4]/section/div/a/@href')
for a in a_list:
    res = requests.get(a,headers=headers)
    tree = etree.HTML(res.content.decode())
    title = tree.xpath()
# print(a_list)
try:
    sql = 'insert into user values(null,"lucky" ,1,1)'
    cursor.execute(sql)  
    print(cursor.rowcount)
    db.commit()
except:
    db.rollback()