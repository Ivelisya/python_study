import os.path
import requests
from concurrent.futures import ThreadPoolExecutor,wait


def do_index_m3u8(path):
    '''
    将index.m3u8写入到ts文件夹内 将ts url改名为 0.ts 1.ts  目的是为了和ts文件中的ts文件进行对象
    '''
    with open('index.m3u8', 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    # 判断 当前存储ts的文件目录是否存在 不存在则创建
    if not os.path.exists(path):
        os.mkdir(path)
    # print(lines)
    file_path = os.path.join(path, 'index.m3u8')
    f = open(file_path, 'w', encoding='UTF-8')
    i = 0
    for line in lines:
        # print(line)
        # 获取所有要下载的ts的url地址  不以#作为开头
        if line.startswith('#'):
            f.write(line)
        else:
            f.write(str(i)+'.ts\n')
            i += 1

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
            res = requests.get(url, headers=headers,timeout = 60)
            print(url, '正在下载')
            # 拼接下载文件的路径及下载后ts的文件名称
            file_path = os.path.join(path, str(i) + '.ts')
            # 进行下载写入
            with open(file_path, 'wb') as f:
                f.write(res.content)
            print('下载成功~')
            break
        except:
            print(url,'请求超时~重新下载中')
def marge(path,filename = 'out'):
    os.chdir(path)
    cmd = f'ffmpeg -i index.m3u8 -c copy {filename}.mp4'
    os.system(cmd)
def download_all_m3u8(path,filename='index.m3u8'):
    '''
    下载所有的m3u8的里面的ts文件
    :param filename: m3u8的文件名称
    :return:
    '''
    # 读取index.m3u8文件  以列表形式返回每一行
    with open(filename, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        # 下载所有ts的文件的路径
    if not os.path.exists(path):
        os.mkdir(path)
    # print(lines)
    # 循环读取每一行数据
    # 创造线程池并发下载
    pool = ThreadPoolExecutor()
    tasks = []
    i = 0
    for line in lines:
        # 获取所有要下载的ts的url地址  不以#作为开头
        if line.startswith('#'):
            continue
        # print(line)
        # 进行下载处理
        url = line.strip()  # 去除请求的url中可能包含的其他的字符
        tasks.append(pool.submit(dowload_one_m3u8,url, i, path))
        i += 1
    wait(tasks)
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    path = 'ts'
    download_all_m3u8(path)
    do_index_m3u8(path)
    marge(path)