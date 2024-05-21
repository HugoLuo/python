# single thread

import time
def mysleep():
    print("hugo")
    time.sleep(3)

def single_demo():
    begin_time=round(time.time())
    mysleep()
    mysleep()
    end_time=round(time.time())
    print("running time is {0}".format(end_time-begin_time))
# print("running in single :")
# single_demo()


import threading
def mutil_threads():
    start_time=round(time.time())
    t1=threading.Thread(target=mysleep)
    t2=threading.Thread(target=mysleep)
    t1.start()
    t2.start()
    finished_time=round(time.time())
    print("running time is {0}".format(finished_time-start_time))
# print("running mutil :")
# mutil_threads()

class MyThread(threading.Thread):
    def run(self):
        time.sleep(2)
        print("running")
def function_for_MyThread():
    # kaishi_time=round(time.time())
    kaishi_time=time.time()
    t1=MyThread()
    t2=MyThread()
    t1.start()
    t2.start()
    t1.join()   #等待线程结束再继续执行程序
    t2.join()   #等待线程结束再继续执行程序
    # jiesu_time=round(time.time())
    jiesu_time=time.time()
    print("running time is {0}".format(jiesu_time-kaishi_time))

function_for_MyThread()