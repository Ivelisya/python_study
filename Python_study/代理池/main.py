'''
项目运行的入口
'''
from multiprocessing import Process
# from get_ip3 import get_ip
from app import run
from test_ip import run as t_run


def main():
    # Process(target=get_ip).start()#开启抓ip的入口
    Process(target=run).start()#开启web测试ip接口的进程
    Process(target=t_run).start()#测试ip
    
if __name__ == '__main__':
    main()