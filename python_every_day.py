
# 2024-5-22 
# 找到最小的那个数字并输出
def min_number():
    number1=int(input("Please enter the first number:"))
    number2=int(input("Please enter the second number:"))
    number3=int(input("Please enter the third number:"))
    if number1 <= number2 and number1 <= number3:
        min_number = number1
    elif number2 <= number1 and number2 <= number3:
        min_number = number2
    else:
        min_number = number3

    print("最小的数字是：%d" %min_number)

# min_number()

def directory_key_and_value():
    data={1:"a",2:"b",3:"c"}
    if "a" in data:  #data 其实就是 data.key()  若想对value 进行查询 ,可用data.values()
        print("a")
    elif "3" in data:
        print("c")
    else:
        print("fail")

    if "a" in data.values():
        print("search by value can find a")
    if 2 in data.keys():
        print("search by key ,can find it<---2 ")
# directory_key_and_value()


def compute():
    a = 100
    b = 0 
    if a > 1:
        a //= 2
        b += 1
    print(a)
    print(b)
# compute()

def list_end_index():
    lists = [1,2,3,]
    a = lists.pop()
    print(a)
# list_end_index()

def type_trans_compare():
    a = float("inf")
    b = a+1
    print(a==b,b-a,b>a)
# type_trans_compare()

def string_index():
    string1="Hello world!"
    a = string1.index("o",5)
    print(a)
# string_index()

def func_list1():
    list1 = [[1,2,3],[4,5,6],[7,8,9]]
    # items = []
    # for item in list1:
    #     for i in item:
    #         items.append(i)
    # OR
    items=[i for item in list1 for i in item]

    print(items)
# func_list1()

def func_list2(lists,items=None):
    if items is None:
        items = []
    for item in lists:
        if type(item) != list:
            items.append(item)
        else:
            func_list2(item,items)
    return items

# res = func_list2([[1,2,3],[4,5],[[7,8,9]]])
# print(res)

def func_list3():
    lists = [True,False,0,None,1]
    result = lists[-1] or lists[0] and lists[2]  #and的优先级高于or, 不是从左到右来进行逻辑运算
    #  上面分成左右两部分： lists[-1]  和 （lists[0] and lists[2]）
    # 左边是1 , 而且后面是or ,就不管右手部分是什么逻辑运算结果，最终的结果就是1    
    print(result)

# func_list3()

import time
def progress():
    for i in range(11):
        progress = "#"*i + "-"*(10-i)
        print(f"{progress}",end=' ')
        time.sleep(0.5)

# progress()

def python_print():
    name = "Hugo"
    print(f"hello {name}")

# python_print()


from tqdm import tqdm
def tqdm_progress():
    # for i in tqdm(range(100)):
    #     time.sleep(0.5)
    pbar = tqdm(total=100)
    for i in range(100):
        pbar.update(1)
        time.sleep(1)

# tqdm_progress()

def print_inf():
    str1 = "world"
    print("Hello {}m ",str1)
# print_inf()

class MyClass:

    pass    

class Person:
    def __init__(self,name,age):  # 初始化出厂配置，对生成的实例进行属性配置
        self.name = name
        self.age = age
        #__init__ 方法不能有返回值 
        print(self,id(self),"~~~")

    def print_person(self):
        print("name=%s,age=%d id=%s" %(self.name,self.age,id(self)))

# p1 = Person('Hugo',42)
# p2 = Person('Amy',30)
# # 类实例化后，得到一个实例对象

# p1.age += 1

# p1.print_person()
# p2.print_person()
# 对象调用方法时，采用p1.print_person()的方式，实例对象回绑定到方法上。print_person的第一参数self其实就就是p1
# print(p1)
# print(p1.age,p1.name)

# print(p2)
# print(p2.age,p2.name)


# print(Person('Candy',30))

# p1.print_person()


# print("ABC".lower())
# print(str.lower("EFG"))



"""
实例化-->初始化实例
或者上述的过程叫做构造化
实例化：
oneOBJ=Person()

初始化：
Person(self,"Hugo",42)

print(MyClass.__name__)

"""

# class People:
#     age = 1
#     height = 170
#     def __init__(self,name,age = 18):
#         self.name = name
#     def print_people(self):
#         print("name=%s age=%d" %(self.name,self.age))
# 1
# p100 = People('P100')
# p100.print_people()

# print(Person)
# print(Person.__name__)
# print(Person.__class__)
# print(Person.__dict__)
'''
特殊属性：
__name__    对象名
__class__   对象的类型
__dict__    对象的属性的字典
__qualname__    类的限定名
'''

class People:
    age = 3
    height = 170
    def __init__(self,name,age=18):
        self.name = name
        self.age = age
tom = People('Tom')
jerry = People('Jerry',20)
People.age = 30
print(1,tom.age,jerry.age)

print(2,People.height,tom.height,jerry.height)

jerry.height=175
print(3,People.height,tom.height,jerry.height)

tom.height += 10
print(4,People.height,tom.height,jerry.height)

People.height += 15
print(5,People.height,tom.height,jerry.height)


# weight是动态添加的类属性
People.weight = 70
print(6,People.weight,tom.weight,jerry.weight)

print(7,tom.__dict__['height'],tom.height)  #两种不同的访问方式，前面是使用字典访问方式，后面是使用属性访问方式

# print(8,tom.__dict__['weight'])   #这样访问是问对象的字典，会报KeyError，应该去访问类的字典或属性
# 以下是基于对象访问动态添加的类属性weight的三种方法
print(8, type(tom).__dict__['weight'],tom.__class__.__dict__['weight'],tom.__class__.weight)

'''总结：是类的，也是所有实例的，类的实例都可以访问；
       是实例的，就是这个实例自己的，通过类访问不到。

       类变量是属于类的变量，这个类的所有实例都可以共享这个变量。

       对象(实例或类)可以动态的给自己添加一个属性(赋值即定义一个属性)
       如上面的People.weight = 70
        实例.__dict__['变量名'] 和 实例.变量名 都可以访问到实例自己的属性(注意这两种方法有本质的区别的)   

       实例的同名变量会隐藏掉类变量，或者说是覆盖了这个类变量。注意⚠️ 类变量还在那里，并没有被真正覆盖。

       实例属性的查找顺序(实例的__dict__  --> 实例的类的__dict__ 优先查找对象自己的，如果没有就找对象所对应的类的)
       指的是实例使用.点号来访问属性，会先找自己的__dict__,如果没有，然后通过__class__找到自己的类，再去类的__dict__中查找

       一般来说，类变量可使用全大写来命名。

'''



