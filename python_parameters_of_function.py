# 编辑python文件  mypram.py
import sys
print(sys.argv)

# 获取参数
# sys.argv表示的含义
print(sys.argv[0])  #获取python的文件名
print(sys.argv[1])  #获取python文件的第一个参数，
print(sys.argv[2])  #获取python文件的第二个参数
print(sys.argv[1:])  #获取所有参数的列表
print(len(sys.argv)-1) #获取参数的个数

pramlen=len(sys.argv)-1

if pramlen != 3:
    print("the number of prameters DO NOT match the request,exit")
    sys.exit(1)
else:
    print("the number of prameters match the request")

# 当执行上面程序时，向该程序传递参数的操作如下：
# python3 mypram.py parameter1 parameter2


# python3 python_parameters_of_function.py parameter1 parameter2
# ['python_parameters_of_function.py', 'parameter1', 'parameter2']
#传进python文件的参数将以列表的方式存储到一个名为argv的列表里




