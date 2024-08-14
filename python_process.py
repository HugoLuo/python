# import os
# import time

# num =1

# def func1():
#     while True:
#         time.sleep(0.5)
#         print("function 1 () ------>")

# def func2():
#     while True:
#         time.sleep(2)
#         print("function 2 () ------>")

# if __name__ == "__main__":

#     pid = os.fork()
#     if pid < 0:
#         print("create failed ")
#     elif pid == 0 :
#         print("this is child process")
#     else:
#         print("this is parent process ")

#     print("******** the end **********")

    # func1()
    # pid = os.fork()
    # print("pid is ",pid)



# def child():
#     print("Hello from child",os.getpid())
#     os._exit(0)

# def parent():
#     pid = os.fork()
#     if pid == 0:
#         child()
#         print("folk child process error!")
#     else:
#         print("Hello from parent",os.getpid(),pid)

# parent()
    

################################################

#process 01
# import os
# from multiprocessing import Process
# from time import sleep

# def task1():
#     while True:
#         sleep(0.5)
#         print('这是任务一...............',os.getpid(),"----------",os.getppid())



# def task2():
#     while True:
#         sleep(2)
#         print('这是任务二...............',os.getpid(),"----------",os.getppid())


# if __name__ == '__main__':
#     print(os.getpid())

#     #子进程
#     p1 = Process(target=task1,name = '任务1')
#     p1.start()
#     print(p1.name)

#     p2 = Process(target=task2,name = '任务2')
#     p2.start()
#     print(p2.name)
    
#     print("------------------------")
#     print("*************************")



#############################################################

#process 02

# import os
# from multiprocessing import Process
# from time import sleep

# def task1(s,name):
#     sleep(s)
#     print("这是任务1。。。。。。。。。。",os.getpid(),'----',os.getppid(),name)

# def task2(s,name):
#     sleep(s)
#     print("这是任务2。。。。。。。。。。",os.getpid(),'----',os.getppid(),name)

# number = 1
# if __name__ == '__main__':
#     print(os.getpid())

#     #子进程
#     p1 = Process(target=task1,name="task1",args=(0.2,'aa'))
#     p1.start()
#     print(p1.name)


#     p2 = Process(target=task2,name="task2",args=(2,'bb'))
#     p2.start()
#     print(p2.name)

#     while True:
#         number += 1
#         sleep(0.2)
#         if number == 20:
#             p1.terminate()
#             p2.terminate()
#             break
#         else:
#             print("------------>number:",number)
#     print("-----------------------------------------")
#     print("*****************************************")




########################################################
# process 03

# import os
# from multiprocessing import Process
# from time import sleep

# m = 1 #不可变类型
# list1 = []  #可变类型

# def task1(s,name):
#     global m
#     while True:
#         sleep(s)
#         m += 1
#         list1.append(str(m)+"task1")
#         print('这是任务1。。。。。。。',m,list1)

# def task2(s,name):
#     global m
#     while True:
#         sleep(s)
#         m += 1
#         list1.append(str(m)+"task2")
#         print('这是任务2。。。。。。。',m,list1)


# if __name__ == '__main__':
#     #子进程
#     p1=Process(target=task1,name='任务1',args=(1,'aa'))
#     p1.start()

#     p2=Process(target=task2,name='任务2',args=(2,'bb'))
#     p2.start()

#     while True:
#         sleep(1)
#         m += 1
#         print('------------>main:',m)



################################################
#process 04
#自定义进程
from collections.abc import Callable
from multiprocessing import Process
from typing import Any, Iterable, Mapping

class MyProcess(Process):
    def __init__(self, name,num):
        super(MyProcess,self).__init__()
        self.name=name
        self.num=num
    
    def run(self):
        n = 1
        while True:
            print('{}--------->自定义进程,n:{}'.format(n,self.name))
            n += 1

if __name__ == "__main__":
    p1 = MyProcess('小明',10)
    p1.start()

    p2 = MyProcess('小红')
    p2.start()

    