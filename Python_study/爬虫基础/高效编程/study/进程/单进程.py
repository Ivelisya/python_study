import time

start = time.time()
def run():
    time.sleep(1)
    
if __name__ == '__main__':
    for i in range(5):
        run()
print(time.time() - start)