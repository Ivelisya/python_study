from concurrent.futures import ThreadPoolExecutor,as_completed
import time
def run(i):
    # print(i,'开始')
    time.sleep(2)
    # print(i,'结束')
    return i
pool = ThreadPoolExecutor(3)
# 方式一
# for i in range(6):
#     pool.submit(run,i)
# pool.shutdown()
# 方式二
# pool.map(run,range(6))
# pool.shutdown
# 方式三
# task = [pool.submit(run, i) for i in range(6)]
# task.shutdown()
# for i in range(6):
task =[pool.submit(run, i) for i in range(6)]
pool.shutdown()
# as_completed 将线程池对象变成迭代器
for i in as_completed(task):
    print(i.result())