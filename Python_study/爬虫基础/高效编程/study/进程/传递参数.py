from multiprocessing import Process

def run(i):
    print(i)

if __name__ == '__main__':
    for i in range(15):
        p = Process(target=run,args=(i,))
        p.start()
    print('over')