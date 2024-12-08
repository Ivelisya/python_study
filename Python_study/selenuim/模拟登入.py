from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import base64
import json
import requests
import time
def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""


if __name__ == "__main__":
    driver = Chrome()
    driver.get('https://www.gushiwen.cn/')
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div/a[6]').click()
    # 获取 用户名 密码 验证码 登入1的节点
    username = '793390457@qq.com'
    userpass = 'xlg17346570232'
    # 下载验证码
    driver.find_element(By.ID,'email').send_keys(username)
    # 获取密码节点 并输入密码
    driver.find_element(By.ID,'pwd').send_keys(userpass)
    # driver.find_element(By.ID,'code').send_keys()
    # 获取验证码图片的节点对象 保存为code.png
    driver.find_element(By.ID,'imgCode').screenshot('code.png')
    img_path = "./code.png"
    result = base64_api(uname='2021223020', pwd='mazyu602', img=img_path, typeid=3)
    # 输入验证码
    driver.find_element(By.ID,'code').send_keys(result)
    driver.find_element(By.ID,'denglu').click()
    
    # 获取登录后的cookie
    cookies = driver.get_cookies()
    json_cookies = json.dumps(cookies) #使cookie使用字符串保存
    # 存储json字符串的cookies
    with open('gsw_cookies.txt','w') as f:
        f.write(json_cookies)
    time.sleep(10)
    