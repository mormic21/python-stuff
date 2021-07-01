import threading
import time

class myFred(threading.Thread):
    Ergebnis = [0, 1]

    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        i = 0
        while i < 20:
            lockMe.acquire()
            zahl = myFred.Ergebnis[len(myFred.Ergebnis) - 2] + myFred.Ergebnis[len(myFred.Ergebnis) - 1]
            myFred.Ergebnis.append(zahl)
            lockMe.release()
            i = i + 1



        #lockMe.acquire()
        #print("Starte" + str(self.id))
        #time.sleep(self.id * 3)
        #lockMe.release()
        #print("Ende" + str(self.id))

if __name__ == '__main__':
    lockMe = threading.Lock()
    t1 = myFred(1, "t1")
    t2 = myFred(2, "t2")

    t1.start()
    t2.start()
    #main geht erst weiter, wenn der jeweilige thread beendet ist
    t1.join()
    #while-schleife anstatt join
   # while t1.isAlive():
       # time.sleep(1)
    t2.join()

    print(myFred.Ergebnis)
   # print("Ende des Main-Threads")
