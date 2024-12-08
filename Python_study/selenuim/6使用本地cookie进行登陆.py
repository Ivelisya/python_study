import time

from selenium.webdriver import Chrome
import json

driver = Chrome()
driver.get('https://so.gushiwen.cn/user/collect.aspx')  # 访问古诗文 我的
time.sleep(2)
# time.sleep(1000)
# 获取cookies
with open('gsw_cookies.txt', 'r') as f:
    cookies = json.loads(f.read())  # 读取所有cookies  转换为列表的cookie

for cookie in cookies:
    cookie_dict = {}
    # print(cookie)
    for k,v in cookie.items():
        cookie_dict[k] = v
    driver.add_cookie(cookie_dict)
driver.refresh()  # 刷新  使我们的cookie生效
# 此刻重新访问我的
driver.get('https://so.gushiwen.cn/user/collect.aspx')