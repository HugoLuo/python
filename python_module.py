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

# 2.自定义模块的引用

# import Python_Object
# programer=Python_Object.Programer("Jimbo","python",45)
# programer.print_info()


# from Python_Object import People
# p1=People("Any",30)
# p1.print_info()

# __name__ 这个系统变量显示了当前模块执行过程中的名称。如果当前程序运行在这个模块中,__name__的名称就是__main__;
#                                               如果不是,则为这个模块的名称

import Python_Object
Python_Object.HaveFun()



# 模块：模块是一个.py的文件，可以包含函数、类、变量等的定义，以及可执行的代码和逻辑。模块可以直接使用import 语句导入。
# 包：包由多个模块和一个__init__.py文件组成的目录，用于将相关的模块组织在一起，包必须包含一个__init__.py的文件，以定义包的属性和方法，
#    包可以使用import 语句导入，也可以使用from 语句导入包中的特定模块。
#    Python2__init__.py才能成为包，Python3无需__init__.py，习惯都包含__init__.py
# #模块是python程序的基本模块，包是组织和重用模块的一种方式。

# from onePackage import oneModule

# 3.第三方模块的引用