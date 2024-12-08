'''
python的web框架
进行请求 返回可用的ip
访问web端口返回可用ip
'''

from gevent import pywsgi
from flask import Flask
from proxy_redis import ProxyRedis
# 类的实例化
app = Flask(__name__)
# 
# 装饰器
@app.route('/get_ip/')
def index():
    
    Pr = ProxyRedis()
    ip = Pr.get_ip()#返回可用性比较强的ip
    if ip:
        return ip    
    return '禁止'
# 只要调用run，就可以运行当前的flask框架
def run():
    app.run()

if __name__ == '__main__':
    app.run(debug = True)#运行flask