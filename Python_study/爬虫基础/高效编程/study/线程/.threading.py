import os
import threading
def run():
    os.system('notepad')
    
if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print('over')