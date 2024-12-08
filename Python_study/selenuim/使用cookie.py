
'''https://so.gushiwen.cn/user/collect.aspx'''
import time
from selenium.webdriver import Chrome
import json
driver = Chrome()
driver.get('https://so.gushiwen.cn/user/collect.aspx')
with open('gsw_cookies.txt','r') as f:
    cookies = json.loads(f.read()) #读取所有cookies转换为列表的cookie
time.sleep(2)
for cookie in cookies:
    cookie_dict = {}
    for k,v in cookie.items():
        cookie_dict[k] = v
    driver.add_cookie(cookie_dict)
time.sleep(2)
driver.refresh()#刷新 使cookie生效
driver.get('https://so.gushiwen.cn/user/collect.aspx')
time.sleep(5)