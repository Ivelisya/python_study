from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
web = Chrome() #实例化
web.get('https://www.baidu.com')
# findelement 返回一个节点对象
# findelements 返回一个列表
# get 获取属性
time.sleep(1000)