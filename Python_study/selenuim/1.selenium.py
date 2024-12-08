from selenium.webdriver.common.by import By
# import time
from selenium.webdriver import Chrome
web = Chrome()
web.get('https://www.gushiwen.cn/')

# # 使用id来查找节点
# txtkey = web.find_element(By.ID,'txtKey')
# # print(txtkey)
# # 向输入框中输入数据
# txtkey.send_keys('唐诗')
# submit = web.find_element(By.XPATH,'//*[@id="search"]/form/input[3]')
# submit.click()
# time.sleep(10)

# 通过超链接内容 获得节点对象
# res = web.find_elements(By.LINK_TEXT,'出其东门')
# print(res)

# 获取页面源码
print(web.page_source)