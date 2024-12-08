import os.path
import re
from urllib.parse import urljoin
import aiohttp
import asyncio
import aiofiles
from aiohttp import TCPConnector

async def get_m3u8_url(url):
    '''
    抓取页面中的index.m3u8的文件数据 写入到本地index.m3u8文件并返回m3u8url地址
    :param url: 页面的url（要抓取的视频的页面url）
    :return: url
    '''
    async with aiohttp.ClientSession(connector=TCPConnector(ssl=False), headers=headers) as session:
        async with session.get(url) as resp:
            data = await resp.text(encoding='UTF-8')
            # 这是抓取第一次的index.m3u8的地址
            index_m3u8_url = re.search('"url":"(.+?index.m3u8)"', data).group(1).replace('\\', '')
            async with session.get(index_m3u8_url) as resp:
                data = await resp.text(encoding='UTF-8')
                index_m3u8_url = urljoin(index_m3u8_url, data.split('/', 3)[-1]).strip()
                # 请求第二个index.m3u8地址，当前返回的内容就是咱们真正获取ts文件的url
                async with session.get(index_m3u8_url) as resp:
                    data = await resp.text(encoding='UTF-8')
                    async with aiofiles.open('index.m3u8', 'w', encoding='UTF-8') as f:
                        await f.write(data)
    return index_m3u8_url


async def dowload_one_m3u8(url, i, path, sem):
    '''
    下载单个ts文件的函数
    :param url: 要下载ts的url地址
    :param i: 当前的文件的名称  也就是i的循环自增
    :param path: 当前下载后ts所需要存储的路径
    :return:
    '''
    while True:
        # 使用信号量 控制并发
            async with sem:
                    try:
                        async with aiohttp.ClientSession(connector=TCPConnector(ssl=False), headers=headers) as session:
                            print(url, '正在下载')
                            async with session.get(url, timeout=60) as resp:
                                    data = await resp.read()
                                    # 拼接下载文件的路径及下载后ts的文件名称
                                    file_path = os.path.join(path, str(i) + '.ts')
                                    # 进行下载写入
                                    async with aiofiles.open(file_path, 'w') as f:
                                        await f.write(data)
                                        print(url, '下载成功~')
                                        break
                    except:
                            print(url, '请求超时~ 重新下载中')

async def download_all_m3u8(path, filename='index.m3u8'):
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
    # 创建信号量 并发下载
    sem = asyncio.Semaphore(100)
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
        tasks.append(asyncio.create_task(dowload_one_m3u8(ts_url, i, path, sem)))
        i += 1
    # 集体等待
    await asyncio.wait(tasks)

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

def merge(path, filename='output'):
    '''
    进行ts文件合并 解决视频音频不同步的问题 建议使用这种
    :param filePath:
    :return:
    '''
    os.chdir(path)  # 进入到ts文件夹 然后执行下面的命令
    cmd = f'ffmpeg -i index.m3u8 -c copy {filename}.mp4'
    os.system(cmd)

async def main(url, path):
    task = asyncio.create_task(get_m3u8_url(url))
    await asyncio.gather(task)
    task = asyncio.create_task(download_all_m3u8(path))
    await asyncio.gather(task)
    do_index_m3u8(path)  # 处理index.m3u8文件
    merge(path, '闪电侠')  # 合并视频


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    url = 'https://www.9meiju.cc/mohuankehuan/shandianxiadibaji/1-1.html'
    path = 'ts'  # 下载所有ts的文件的路径
    asyncio.run(main(url, path))
    # get_m3u8_url(url)
    # download_all_m3u8(path)  # 下载所有视频
    # do_index_m3u8(path)  # 处理index.m3u8文件
    # merge(path)  # 合并视频
    # ts 下载后的样子
    # 0.ts 1.ts  2.ts