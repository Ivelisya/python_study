from multiprocessing import Process,Manager
# 放入put 获取get
def run(d):
    d.put('name')
    d.put('age')
    d.put('sex')

if __name__ == '__main__':
    # 创建可通信队列
    d = Manager().Queue()
    print(d)
    # exit()
    p = Process(target=run,args=(d,))
    p.start()
    p.join()
    # 如果队列中没有数据，会阻塞等待
    print(d.get())
    print(d.get())
    print(d.get())
    # print(d.get(timeout=3))
    #阻塞等待时间3秒
    print('over')
    try:
        print(d.get(timeout=3))#阻塞等待时间3秒
    except:
        pass
