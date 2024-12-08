import requests
head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
    # 'Cookie':'GUID=f8524e09-2cef-469b-9130-1f928932a87d; Hm_lvt_9793f42b498361373512340937deb2a0=1693810561; sajssdk_2015_cross_new_user=1; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F18%252F98%252F90%252F96139098.jpg-88x88%253Fv%253D1650527904000%26id%3D96139098%26nickname%3D%25E4%25B9%25A6%25E5%258F%258BqYx51ZhI1%26e%3D1709363090%26s%3D5330662c27094c32; c_channel=0; c_csc=web; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2296139098%22%2C%22%24device_id%22%3A%2218a5efa0f5271e-01082062ab8926-7f5d5470-1296000-18a5efa0f53533%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22f8524e09-2cef-469b-9130-1f928932a87d%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1693811426'
}
url = 'https://passport.17k.com/ck/user/login'
data = {
    'loginName': '17346570232',
    'password': 'xlg17346570232'
}
session = requests.Session()
session.post(url,headers=head,data=data)
url = 'https://user.17k.com/ck/user/myInfo/96139098?bindInfo=1&appKey=2406394919'
res = session.get(url,headers=head)
print(res.json())