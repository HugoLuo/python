# # Python Object

# name="Hugo"
# age=42
# # print("name is "+name+" Age is "+age)
# print("name is {0} age is {1}".format(name,age))

#define class
class MyPeople:
    name="hugo"
    age=42
    def print_info(self):
        print("My name is {0} and age is {1}".format(self.name,self.age))


# #instance class
# oneObject=MyPeople()
# oneObject.name="boss"
# oneObject.age=25
# oneObject.print_info()

# 定义一个普通类
class Person:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def print_info(self):
        print("My name is {0} and age is {1}".format(self.name,self.age))

# obj=Person("Jon",23)
# obj.name="Domina"
# obj.print_info()

#__隐藏属性的使用
class People:
    def __init__(self,name,age=30):
        self.__name=name
        self.__age=age
    def print_info(self):
        print("My name is {0} age is {1}".format(self.__name,self.__age) )

# people=People('Amy')
# people.__name="Candy"
#使用__隐藏属性，实例就无法直接操作
# people.print_info()

#类提供方法去访问或设置类属性
class Zoo:
    def __init__(self,name,age=1) -> None:
        self.__name=name
        self.__age=age
    
    def set_name(self,name):
        self.__name=name
    
    def set_age(self,age):
        self.__age=age
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def print_info(self):
        print("the zoo name is {0} age is {1}".format(self.__name,self.__age))

# dog=Zoo('Dog',3)
# dog.print_info()


# 类的封装，隐藏的方法，方法智能在类内部使用
class Animal:
    def __init__(self,name,age) -> None:
        self.__name=name
        self.__age=age
    
    #通过在方法前加一个下划线定一个隐藏的方法，该方法只能被类内部使用。
    #隐藏方法可以在类内部做一些内部操作或运算。
    def _private(self):
        print("内部方法被调用")
    
    #在一般的类方法里可以访问类内定义的隐藏方法
    def call_private_func(self):
        self._private()

# animal=Animal("cat",1)
# #调用类的一般方法
# animal.call_private_func()


#类的继承
# class Programer(People):
#     pass

class Programer(Zoo):

    def __init__(self, name, type,age=1) -> None:
        super().__init__(name, age)
        #在新类中定义自己的新增属性
        self.type=type

    #在新的类中，定义自己独有的方法
    def coding(self):
        print("程序员有独有的技能coding")
    
    #在新的类中，重写父类中的方法
    def print_info(self):
        print("the name is {0} age is {1} have new function {2} {3}".format(self.get_name(),self.get_age(),"coding",self.type))

# #使用新的类，创建实例对象
# programer=Programer("Hugo",42)
# programer.print_info()

# #调用父类中的方法
# programer.print_info()

# #调用自己独有的方法
# programer.coding()

programer=Programer("Hugo","Python",42)
programer.print_info()








