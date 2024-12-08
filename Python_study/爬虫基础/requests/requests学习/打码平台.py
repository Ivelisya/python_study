import base64
import json
import requests
# 一、图片文字类型(默认 3 数英混合)：
# 1 : 纯数字
# 1001：纯数字2
# 2 : 纯英文
# 1002：纯英文2
# 3 : 数英混合
# 1003：数英混合2
#  4 : 闪动GIF
# 7 : 无感学习(独家)
# 11 : 计算题
# 1005:  快速计算题
# 16 : 汉字
# 32 : 通用文字识别(证件、单据)
# 66:  问答题
# 49 :recaptcha图片识别
# 二、图片旋转角度类型：
# 29 :  旋转类型
#
# 三、图片坐标点选类型：
# 19 :  1个坐标
# 20 :  3个坐标
# 21 :  3 ~ 5个坐标
# 22 :  5 ~ 8个坐标
# 27 :  1 ~ 4个坐标
# 48 : 轨迹类型
#
# 四、缺口识别
# 18 : 缺口识别（需要2张图 一张目标图一张缺口图）
# 33 : 单缺口识别（返回X轴坐标 只需要1张图）
# 五、拼图识别
# 53：拼图识别
def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        #！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]
    return ""


if __name__ == "__main__":
    # 下载验证码
    session = requests.Session()
    url = 'https://so.gushiwen.cn/RandCode.ashx?'
    res = session.get(url)
    with open('./yzm.jpg','wb') as fp:
        fp.write(res.content)   
    # 识别验证码
    head = {
        'Referer':'https://so.gushiwen.cn/user/login.aspx?',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
    }
    img_path = "./yzm.jpg"
    result = base64_api(uname='2021223020', pwd='mazyu602', img=img_path, typeid=3)
    print(result)
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
    data = {
        '__VIEWSTATE':'8Lawfyf1/R1O1JfsM5Tg+hqxIuoWplqxkTBnAqeZWrC8fGAy9Zhd1UWPiFH8sVoTWLujA0yYy9GiLwGAexol2M6Msae8XBTnqkzhkkej//O8itoyQbgvXEVIQwR/Yw1ye2kjecg7bDfhv+pcE5rJ500nwT8=',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from':'http://so.gushiwen.cn/user/collect.aspx',
        'email':'2021223020@qq.com',
        'pwd':'mazyu602',
        'code':result,
        'denglu':'登录'
      }
    res = session.post(url,headers=head,data=data)
    print(res.content.decode())
    with open('2.text','wb') as fb:
        fb.write(res.content)
    