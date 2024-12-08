import threading
def run(i):
       print(i)
       
if __name__ =='__main__':
    t = threading.Thread(target=run,args=(1,))
    t.start()
    t.join()