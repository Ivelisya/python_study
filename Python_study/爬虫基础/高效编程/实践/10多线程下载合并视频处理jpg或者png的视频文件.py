import os.path
import requests
import re
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor, wait


def get_m3u8_url(url):
    '''
    抓取页面中的index.m3u8的文件数据 写入到本地index.m3u8文件并返回m3u8url地址
    :param url: 页面的url（要抓取的视频的页面url）
    :return: url
    '''
    res = requests.get(url, headers=headers,verify=False)
    data = res.content.decode()  # 抓取页面内容

    # 这是抓取第一次的index.m3u8的地址
    index_m3u8_url = re.search('"url":"(.+?index.m3u8)"', data).group(1).replace('\\', '')

    # 进行请求  获取第二次index.m3u8的url地址
    res = requests.get(index_m3u8_url, headers=headers)
    data = res.content.decode()  # 抓取页面内容
    # 拼接第二次请求的m3u8文件地址
    # print(index_m3u8_url.rsplit('/', 1)[0]+'/'+data.split('/', 3)[-1].strip())
    index_m3u8_url = urljoin(index_m3u8_url, data.split('/', 3)[-1]).strip()
    # 请求第二个index.m3u8地址，当前返回的内容就是咱们真正获取ts文件的url
    res = requests.get(index_m3u8_url, headers=headers)
    data = res.content.decode()  # 抓取页面内容
    with open('index.m3u8', 'w', encoding='UTF-8') as f:
        f.write(data)
    return index_m3u8_url


def dowload_one_m3u8(url, i, path):
    '''
    下载单个ts文件的函数
    :param url: 要下载ts的url地址
    :param i: 当前的文件的名称  也就是i的循环自增
    :param path: 当前下载后ts所需要存储的路径
    :return:
    '''
    while True:
        try:
            res = requests.get(url, headers=headers, timeout=60)
            print(url, '正在下载')
            # 拼接下载文件的路径及下载后ts的文件名称
            file_path = os.path.join(path, str(i) + '.ts')
            # 进行下载写入
            with open(file_path, 'wb') as f:
                f.write(res.content)
            print(url, '下载成功~')
            break
        except:
            print(url, '请求超时~ 重新下载中')

def download_all_m3u8(path, filename='index.m3u8'):
    '''
    下载所有的m3u8的里面的ts文件
    :param path: 存储下载ts文件的文件夹
    :param filename: m3u8的文件名称
    :return:
    '''
    # 读取index.m3u8文件  以列表形式返回每一行
    with open(filename, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    # 判断 当前存储ts的文件目录是否存在 不存在则创建
    if not os.path.exists(path):
        os.mkdir(path)
    # print(lines)
    # 创建线程池 并发下载
    pool = ThreadPoolExecutor(100)
    tasks = []
    # 循环读取每一行数据
    i = 0
    for line in lines:
        # 获取所有要下载的ts的url地址  不以#作为开头
        if line.startswith('#'):
            continue
        # print(line)
        # 进行下载处理
        ts_url = line.strip()  # 去除请求的url中可能包含的其他的字符
        tasks.append(pool.submit(dowload_one_m3u8, ts_url, i, path))
        i += 1
    # 集体等待
    wait(tasks)

def do_index_m3u8(path, filename='index.m3u8'):
    '''
    将index.m3u8写入到ts文件夹内 将ts url改名为 0.ts 1.ts  目的是为了和ts文件中的ts文件进行对象
    '''
    with open(filename, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    # 判断 当前存储ts的文件目录是否存在 不存在则创建
    if not os.path.exists(path):
        os.mkdir(path)
    # print(lines)
    file_path = os.path.join(path, filename)
    f = open(file_path, 'w', encoding='UTF-8')
    i = 0
    for line in lines:
        # 获取所有要下载的ts的url地址  不以#作为开头
        if line.startswith('#'):
            f.write(line)
        else:
            f.write(str(i)+'.ts\n')
            i += 1

# 解析伪装成png的ts
def resolve_ts(src_path, dst_path):
    '''
    如果m3u8返回的ts文件地址为
    https://p1.eckwai.com/ufile/adsocial/7ead0935-dd4f-4d2f-b17d-dd9902f8cc77.png
    则需要下面处理后 才能进行合并
    原因在于 使用Hexeditor打开后，发现文件头被描述为了PNG
    在这种情况下，只需要将其中PNG文件头部分全部使用FF填充，即可处理该问题
    :return:
    '''
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)
    file_list = sorted(os.listdir(src_path), key=lambda x: int(x.split('.')[0]))
    for i in file_list:
        origin_ts = os.path.join(src_path, i)
        resolved_ts = os.path.join(dst_path, i)
        try:
            infile = open(origin_ts, "rb")  # 打开文件
            outfile = open(resolved_ts, "wb")  # 内容输出
            data = infile.read()
            outfile.write(data)
            outfile.seek(0x00)
            outfile.write(b'\xff\xff\xff\xff')
            outfile.flush()
            infile.close()  # 文件关闭
            outfile.close()
        except:
            pass
        print('resolve ' + origin_ts + ' success')

def merge(path, filename='output'):
    '''
    进行ts文件合并 解决视频音频不同步的问题 建议使用这种
    :param filePath:
    :return:
    '''
    os.chdir(path)  # 进入到ts文件夹 然后执行下面的命令
    cmd = f'ffmpeg -i index.m3u8 -c copy {filename}.mp4'
    os.system(cmd)



if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    url = 'https://www.9meiju.cc/mohuankehuan/shandianxiadibaji/1-1.html'
    get_m3u8_url(url)
    path = 'ts'  # 下载所有ts的文件的路径
    download_all_m3u8(path)  # 下载所有视频
    dst_path = path+'2'  # 当前替换处理完以后的文件路径
    resolve_ts(path, dst_path)  # 处理伪装的jpg或者png的文件数据
    do_index_m3u8(dst_path)  # 处理index.m3u8文件
    merge(dst_path)  # 合并视频
    # ts 下载后的样子
    # 0.ts 1.ts  2.ts
    