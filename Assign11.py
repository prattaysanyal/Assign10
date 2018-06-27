#question1
import datetime
import threading
import time
def task():
    for i in range(3):
        print("thread is starting",datetime.datetime.now())
        time.sleep(5)
    print("thread ends",datetime.datetime.now())

task()

#question2
import threading
import time
import datetime
def task():
    for i in range(1,11):
        print("number is %d"%(i),datetime.datetime.now())
        time.sleep(1)

task()

#question3
import datetime
import time
l=[1,2,3,4,5]
n=int(input("enter the number of intervals"))
for i in l:
    for j in range(4):
            print(i,datetime.datetime.now())
            time.sleep(j*2)
            

#question4
import threading
import time
class task(threading.Thread):
    def __init__(self,num):
        self.num=num
        threading.Thread.__init__(self)
    def fact(self):
        if(self.num==1):
            return self.num
        else:
            return self.num*fact(self.num-1)
    def run(self):
        self.fact()
        

thread1=task(4)
thread1.start()




    


    

    

