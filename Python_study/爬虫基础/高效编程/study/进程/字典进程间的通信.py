from multiprocessing import Process,Manager

def run(d):
    d['name']= '18'

if __name__ == '__main__':
    # 创建可通信字典
    d = Manager().dict()
    print(d)
    # exit()
    p = Process(target=run,args=(d,))
    p.start()
    p.join()
    print(d)
