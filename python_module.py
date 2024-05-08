#1.内置模块的引用

import keyword
#print(keyword.kwlist)

import math
result1=math.ceil(5/3)
result2=math.floor(5/4)
result3=round(2.15)
# print(result1)
# print(result2)
# print(result3)

#Python3中的时间模块time
## 1.格式化日期、时间
## 2.time模块还包含了休眠的功能
import time
# print(time.time())  #1970年1月1日经历的秒数，也就是时间戳
# print(time.localtime())
# print(time.localtime().tm_mon)
# print(time.localtime().tm_mday)
# print(time.localtime().tm_wday)
# 格式化的语法
# %Y:  四数年
# %m: 两数月
# %d:  两数天
# %H: 两数时
# %M: 两数分
# %S: 两数秒
# %s: 时间戳

current_time=time.localtime(time.time())
format_current_time=time.strftime("%Y-%m-%d %H:%M:%S",current_time)
# print(format_current_time)

current_time2=time.localtime(time.time()-3600)
format_current_time2=time.strftime("%Y-%m-%d %H:%M:%S",current_time2)
# print(format_current_time2) 


#将字符串转换成时间戳
time_str="2019-05-18 18:26:29"
time_format="%Y-%m-%d %H:%M:%S"
time_result=time.strptime(time_str,time_format)
# print(time_result)
time_stamp=time.mktime(time_result)
# print(time_stamp)

#死循环加sleep
def dea_loop():
    while True:
        print("Hugo")
        time.sleep(1)

#dea_loop()


#用时间戳去计算程序运行的时间

def computer_time():
    # start_time=time.localtime(time.time())
    start_time=round(time.time())
    # format_start_time=time.strftime("%Y-%m-%d %H:%M:%S",start_time)
    # print(format_start_time)

    time.sleep(1)
    #sleep函数支持浮点数
    time.sleep(0.5)
    # end_time=time.localtime(time.time())
    end_time=round(time.time())
    # format_end_time=time.strftime("%Y-%m-%d %H:%M:%S",end_time)
    # print(format_end_time)
    # used_time=end_time-end_time
    print("this program used time {0:.3f}s".format(end_time-start_time))
# computer_time()

# 用time产生随机数
def general_random_number():
    rdnumber=round(time.time()*100000)
    print(str(rdnumber)[-6:])

general_random_number()

# 2.自定义模块的引用

# import Python_Object
# programer=Python_Object.Programer("Jimbo","python",45)
# programer.print_info()


# from Python_Object import People
# p1=People("Any",30)
# p1.print_info()

# __name__ 这个系统变量显示了当前模块执行过程中的名称。如果当前程序运行在这个模块中,__name__的名称就是__main__;
#                                               如果不是,则为这个模块的名称

# import Python_Object
# Python_Object.HaveFun()



# 模块：模块是一个.py的文件，可以包含函数、类、变量等的定义，以及可执行的代码和逻辑。模块可以直接使用import 语句导入。
# 包：包由多个模块和一个__init__.py文件组成的目录，用于将相关的模块组织在一起，包必须包含一个__init__.py的文件，以定义包的属性和方法，
#    包可以使用import 语句导入，也可以使用from 语句导入包中的特定模块。
#    Python2__init__.py才能成为包，Python3无需__init__.py，习惯都包含__init__.py
# #模块是python程序的基本模块，包是组织和重用模块的一种方式。

# from onePackage import oneModule



# 3.第三方模块的引用