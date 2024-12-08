from multiprocessing import Pool
import time
    
    
    
def run(i):
    print(i)
    time.sleep(5)
if __name__ == '__main__':
    pool = Pool()
    args = [1,2,3,4,5]
    pool.map(run,args)