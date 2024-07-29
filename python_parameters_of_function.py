# 编辑python文件  mypram.py
# import sys
# print(sys.argv)

# # 获取参数
# # sys.argv表示的含义
# print(sys.argv[0])  #获取python的文件名
# print(sys.argv[1])  #获取python文件的第一个参数，
# print(sys.argv[2])  #获取python文件的第二个参数
# print(sys.argv[1:])  #获取所有参数的列表
# print(len(sys.argv)-1) #获取参数的个数

# pramlen=len(sys.argv)-1

# if pramlen != 3:
#     print("the number of prameters DO NOT match the request,exit")
#     sys.exit(1)
# else:
#     print("the number of prameters match the request")

# 当执行上面程序时，向该程序传递参数的操作如下：
# python3 mypram.py parameter1 parameter2


# python3 python_parameters_of_function.py parameter1 parameter2
# ['python_parameters_of_function.py', 'parameter1', 'parameter2']
#传进python文件的参数将以列表的方式存储到一个名为argv的列表里

aa = 1000
def funcA():

    global aa 
    aa = 10001

    bb = 2000
    def funcB():
        nonlocal bb
        bb = 20001
        cc = 3000
        print(aa,bb,cc)

    funcB()
    print(bb)
# funcA()
# print(aa)

def funcB():
    list1 = [1,'b',"c"]
    direct1 = {'e1':"element1",'e2':'element2','e3':'element3'}
    print("func B")
    for i in list1:
        print(i)
    for i in direct1:
        print(i)
    
    return True

# funcB()

# from collections import Iterable
# from time import time
# a = 123
# # print(isinstance(a,Iterable))
# print(time)



# out_var=100
# def out_func():
#     in_var=1000
#     def inner_func():
#         inner_var=10000
#         print("var_var=%s in_var=%s inner_var=%s" %(out_var,in_var,inner_var))
#         print("inner func been call")
#     return inner_func

# x = out_func()
# x_result = x()
# print(x)
# print(x_result)



# def out_func(b,c):
#     out_a=100
#     def innr_func():
#         result = out_a + b + c
#         print("result = {}".format(result))
#     return innr_func

# ifunc=out_func(200,300)
# ifunc()



# def func(a, b):
#     c = 10

#     def inner_func():
#         s = a + b + c
#         print('相加之后的结果是:', s)

#     return inner_func


# # 调用func
# ifunc = func(6, 9)  # ifunc就是inner_func   ifunc = inner_func

# # 调用返出来的内部函数
# ifunc()



# def out_func(a,b):
#     c = 100
#     def inn_func():
#         s = a + b + c 
#         print("the result is %s",s)
    
#     return inn_func
# #这仅仅是将闭包内部函数的地址给one
# one = out_func(20,80)
# two = out_func(30,40)
# three = out_func(30,40)
# print("the one is ",one)
# #这才是通过one的地址，调用其说指向的函数。
# one()

# two()

# three()


# #计数器
# def generate_count():
    
#     container = [0]
    
#     def add_one():
#         container[0] = container[0] + 1
#         print("current is {} times access ".format(container[0]))

#     return add_one

# counter = generate_count()
# counter()
# counter()
# for i in range(10):
#     counter()

# list20=[2,3,57]
# # list30=filter(lambda x:x+2,list20)


# # list200=filter(lambda x:x%2 == 0,list20)
# # print(list200)
# list21=[i+2 for i in list20]
# print(type(list21))
# print(list21)












