import _thread
import os
import time

def run():
    os.system('notepad')
_thread.start_new_thread(run,())
# time.sleep(100)
print('over')