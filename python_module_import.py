#导入模块的三种方法

#  import 模块（加载同一个文件夹内的pyhton文件，这里的模块就是，python文件不带.py的部分 ）

'''
加载模块时，若不对加载进行下列的__all__进行定义，则默认会加载所有的变量、函数、类，有执行的语句，也将会一并执行。
    1.若要对加载进行限制🚫，则对 __all__进行定义，如下：
        __all__=[变量1，变量名2，方法1，方法2，类1，类2....]
    2. __name__记录着当前文件所执行的名字，若是作为主程序则其值是"__main__" ;否则其将作为模块，其值就是模块的名字
    3.基于上面👆第二点，若想将该python程序主方法（即程序入口），则通过对__name__进行判断是否是"__main__" 进而确认是否执行后面的方法，如下：
        if __name__ == "__main__":   #即该文件作为程序主方法(程序入口),执行后面的方法
            func()
    4.或者换种说法，若想python文件中的方法调用，在被作为模块导入时不被执行，则在方法调用前面加上if __name__ == "__mian__"进而限制。如下：
        if __name__ == "__main__":
            func()
        这样只有上面代码作为主程序/程序的入口时，上面的方法调用func() 才会被调用执行。否则上面代码所在的python文件将作为模块导入。func()将不会被执行。
    5.一个python文件被视为一个模块
        
    '''





'''
    1. import python文件名（不带.py的那部分）  ｜ import 模块

    2. from 模块 import 模块里的变量/方法/类
        例如:from python_module import VAR1
            from python_module import onefunc
            from python_module import OneClass
            from python_module import VAR1,OneClass
            from python_module import *
    3. from 模块.类 import *
        例如: from python_module.OneClass import *
'''



import python_module_package   
#上面的第一种情况
print(__name__)

python_module_package.onefunc()