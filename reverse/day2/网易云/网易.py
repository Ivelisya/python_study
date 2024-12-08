import json
import subprocess
from functools import partial
import execjs
import requests
from tqdm import tqdm
import os
import re
from lxml import etree

# 调整subprocess.Popen以使用UTF-8编码
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
# 常用的请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36"
}
def get_song_id_name():
    """从网易云音乐发现页面获取歌曲ID和名称。"""
    resp = requests.get("https://music.163.com/discover", headers=headers)
    tree = etree.HTML(resp.text)
    li_list_ele = tree.xpath('//*[@id="top-flag"]/dl/dd/ol')
    ids = []
    all_names = []
    for li_list in li_list_ele:
        for li in li_list:
            ids.append(li.xpath("./div/a[1]/@data-res-id")[0])
            all_names.append(li.xpath("./a/@title")[0])
    return ids, all_names
def get_url(ids):
    """为给定的歌曲ID生成下载URL。"""
    js = execjs.compile(open('网易.js', mode='r', encoding='utf-8').read())
    data = {
        "ids": json.dumps(ids),
        "level": "standard",
        "encodeType": "aac",
        "csrf_token": ""
    }
    enc_data = js.call('fn', json.dumps(data))
    real_data = {"params": enc_data['encText'], "encSecKey": enc_data['encSecKey']}
    url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
    resp = requests.post(url, data=real_data, headers=headers)
    urls, free_ids = [], []
    for data in resp.json().get('data', []):
        if 'url' in data:
            urls.append(data['url'])
            free_ids.append(data['id'])
        else:
            print(f"没有找到歌曲ID为 {data['id']} 的下载URL")
    return urls, free_ids
def download_music(urls, names):
    """从提供的URL下载音乐。"""
    for index, (url, name) in enumerate(zip(urls, names), start=1):
        cleaned_filename = re.sub(r'[\\/*?:"<>|]', '', name)  # 清理文件名中的非法字符
        file_path = f"D:\\smzy\\music\\{cleaned_filename}.m4a"
        if not os.path.exists(file_path):
            resp = requests.get(url, stream=True)
            if resp.status_code == 200:
                total_size = int(resp.headers.get('Content-Length', 0))
                with open(file_path, 'wb') as f, tqdm(total=total_size, unit='B', unit_scale=True, desc=f"正在下载 {name}") as pbar:
                    for chunk in resp.iter_content(chunk_size=1024):
                        f.write(chunk)
                        pbar.update(len(chunk))
        else:
            print(f"{file_path} 已经存在")
ids,song_names = get_song_id_name()
id_name = zip(ids, song_names)
urls,free_id = get_url(ids)
print(free_id)
id_to_name = dict(id_name)
# 选出 free_id 对应的 name，装入新列表
free_name = [id_to_name[str(free_id_val)] for free_id_val in free_id if str(free_id_val) in id_to_name]
download_music(urls, free_name)



