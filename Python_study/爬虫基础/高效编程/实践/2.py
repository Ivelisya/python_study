import requests
import os
headers = {
        'Referer':'https://so.gushiwen.cn/user/login.aspx?',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
    }
path = 'ts'
if not os.path.exists(path):
    os.makedirs(path)
def download_video():
    with open('index.txt','r',encoding='utf-8') as f:
        lines = f.readlines()
        i = 0
        
        for line in lines:
            if line.startswith('#'):
                continue
            url = line.strip()
            res = requests.get(url,headers=headers)
            file_path = os.path.join(path,str(i)+'.ts')
            with open(file_path,'wb') as f:
                f.write(res.content)
            i += 1
# startswith 