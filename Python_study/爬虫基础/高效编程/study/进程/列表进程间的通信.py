from multiprocessing import Process,Manager
def run(l):
    for i in range(10):
        print(i,'被添加')
        l.append(i)

if __name__=='__main__':
    # 列表共享
    # 创建可通信列表
    l = Manager().list()
    print(l)
    p = Process(target=run,args=(l,))
    p.start()
    p.join()
    print('over')
    print(l)