import os

def do_index_m3u8():
    '''
    将index.m3u8写入到ts文件夹内 将ts url改名为 0.ts 1.ts  目的是为了和ts文件中的ts文件进行对象
    '''
    with open('index.m3u8', 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    path = 'ts'
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
            continue
        else:
            f.write(str(i)+'.ts\n')
            i += 1
