#question1

import threading
import time
class Mythread(threading.Thread):
    def __init__(self,value):
        threading.Thread.__init__(self)
        self.v=value

    def run(self):
        time.sleep(5)
        print("value is" , self.v)

thread1=Mythread(4)
thread1.start()

#question2

import threading
import time
class Mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(1,10):
            print(i)
            time.sleep(1)

thread1=Mythread()
thread1.start()

#question3

import threading
import time


class Mythread(threading.Thread):
    def __init__(self,value):
        threading.Thread.__init__(self)
        self.v=value

    def run(self):
        l=[2,4,6,8,10]
        for i in range (0,5):
            print(self.v[i])
            time.sleep(l[i])


thread1=Mythread([1,2,3,4,5])
thread1.start()



#question4

import threading
import time
import math
class Mythread(threading.Thread):
    def __init__(self,value):
        threading.Thread.__init__(self)
        self.v=value

    def run(self):
         print(math.factorial(self.v))

thread1=Mythread(5)
thread1.start()


