import threading
name = '1'
def run():
    global name
    print(name)
    name = '2'
    print(name)
if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print(name)            