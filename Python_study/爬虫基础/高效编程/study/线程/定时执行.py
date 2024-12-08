import threading
def run():
    print('run')
    
    
if __name__ == '__main__':
    t = threading.Timer(3,run)
    t.start()