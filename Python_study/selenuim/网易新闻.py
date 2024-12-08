from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
driver = Chrome()
driver.get('https://news.163.com/')

# 使用js实现滚动条自动往下
def scroll_windo():
    '''使窗口不断向下滚动'''
    step_length = 2000#每次向下滚动的步长
    stop_length = 20000
    while True:
        if stop_length:
            if stop_length - step_length <= 0:
                driver.execute_script(f'window.scrollBy(0,{stop_length})')
                break
            driver.execute_script(f'window.scrollBy(0,{step_length})')
            time.sleep(0.2)
            stop_length -= step_length