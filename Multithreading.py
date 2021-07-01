import threading
import time

class myFred(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        lockMe.acquire()
        print("Starte" + str(self.id))
        time.sleep(self.id * 3)
        lockMe.release()
        print("Ende" + str(self.id))

if __name__ == '__main__':

    lockMe = threading.Lock()


    t1 = myFred(1, "t1")
    t2 = myFred(2, "t2")

    t1.start()
    t2.start()
    #main geht erst weiter, wenn der jeweilige thread beendet ist
    t1.join()
    t2.join()

    print("Ende des Main-Threads")
