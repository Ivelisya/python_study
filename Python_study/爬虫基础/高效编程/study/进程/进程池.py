from multiprocessing import Pool,cpu_count
import time
    
    
    
def run(i):
    print(i)
    time.sleep(5)
if __name__ == '__main__':
    # 默认的并发数为核心数
    print('你的电脑核心数',cpu_count())
    # pool = Pool()#默认核心并发
    pool = Pool(3)
    # 创建十个进程  
    for i in range(1,11):
        # 将任务放进进程池
        pool.apply_async(run,args=(i,))
    pool.close()#关闭进程次
    pool.join()#阻塞等待
    print('over')
    