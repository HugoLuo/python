
class Person:

    #魔术方法，为创建对象向系统申请内存资源，在创建一个新对象时调用，调用为了开辟空间返回将给__init__方法使用
    def __new__(cls, *args, **kwargs):
        print("--->__new__")
        return object.__new__(cls)

    #魔术方法,类似Java中的构造方法，在对象被初始化时被调用。
    def __init__(self, name1):
        self.name = name1
        print("--->__init__")

    #实例对象作为函数调用时被调用 
    #
    def __call__(self):
        print("--->__call__")

        

    #魔术方法，重写该方法后，当打印对象时返回对应的内容，而非对象的地址。
    def __str__(self) -> str:
        return "this object's name is {}".format(self.name)

import inspect
print(inspect.getmro(Person))
# import sys



# p = Person("Hugo")
# # print(sys.refercount(p1))
# print(p)

# p()


# class A:
#     def test(self):
#         print("A------>test")

# class B(A):
#     def test(self):
#         print("B-------->test")
# class C(A):
#     def test(self):
#         print("C-------->test")

# class D(B, C):
#     def test(self):
#         print("D--------->test")

# d=D()
# d.test()
# print(D.__mro__)


#多继承方式及顺序
#广度优先  深度优先
'''
    A               
   B  C
     D
广度优先： D ->B -> C -> A
深度优先： D ->B -> A -->C
'''



# class Product:

#     def __init__(self,name,price) -> None:
#         self.__price = price
#         self.__name = name
#         self.__color = 'white'
#         self.__meta = "suliao"
#         self.__size = "125*80"

#     def setPrice(self,newprice):
#         self.__price=newprice
    
#     def getPrice(self):
#         return self.__price
    
#     def setName(self,name):
#         self.__name=name

#     def getName(self):
#         return self.__name
    
#     def setColor(self,color):
#         self.__color=color
#     def getColor(self):
#         return self.__color
    
#     #装饰器,现有getXXX
#     @property
#     def meta(self):
#         return self.__meta
#     #再有要装饰属性的set, set依赖于get
#     @meta.setter
#     def meta(self,newMeta):
#         self.__meta = newMeta


#     @property
#     def size(self):
#         return self.__size
#     @size.setter
#     def size(self,newSize):
#         self.__size=newSize
    
    
#     def __str__(self) -> str:
#         return "product's name is {} , price is {}, color is {} ,mate is {}".format(self.__name,self.__price,self.__color,self.__meta)


# product1 = Product('appple',6000)
# print(product1.getPrice())
# print("the product {} ,its price is {}  its color is{}".format(product1.getName(),product1.getPrice(),product1.getColor()))
# product1.setPrice(4000.89)
# print("the product {} ,its price is {}".format(product1.getName(),product1.getPrice()))
# print("******")
# print(product1)

# print("======================================")
# print("Below is class Product  dir(Product)    :")
# print(dir(Product))
# print("--------------------------------------")
# print("below is the object product1  dir(product1):")
# print(dir(product1))
# print("######################################")
# print("below is the __dir__()")
# print(product1.__dir__())
# print("below is the __name__")
# print(__name__)

# product1.meta="taihejin"
# print("product meta is {}".format(product1.meta))

# product1.size="1030*85"
# print("product size is {}".format(product1.size))



# class Pet:
#     def __init__(self,name) -> None:
#         self.__name = name
#     def move(self):
#         print("there are one Pet is move")
    
#     def __str__(self) -> str:
#         return self.__name
    

# class Dog(Pet):
#     def move(self):
#         print("there are one Dog is move")

# class Cat(Pet):
#     def move(self):
#         print("there are one Cat is move")


# class Person:
    
#     def __init__(self,name,pet) -> None:
#         self.__name = name
#         self.__pet = pet
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,name):
#         self.__name = name

#     @property
#     def pet(self):
#         return self.__pet
#     @pet.setter
#     def pet(self,pet):
#         self.__pet = pet
         

#     def __str__(self) -> str:
#         return "the Person {} have pet {}".format(self.name,self.pet)


# class CatZoo:
#     def __init__(self,name) -> None:
#         self.__name = name
#     def __str__(self) -> str:
#         return "this is 猫科动物"
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,name):
#         self.__name = name

# class Bao(CatZoo):
#     def __str__(self) -> str:
#         return "this is 豹 {}".format(self.name)

# class Tiger(CatZoo):
#     def __str__(self) -> str:
#         return "this is 老虎 {}".format(self.name)

# dog = Dog("dog1")
# person = Person("Hugo",dog)
# animal1 = Bao("BAO")

# if isinstance(animal1,Pet):
#     print(person)
#     print("{} is one intance of Pet".format(animal1))
# else:
#     print("{} not a Pet /or Pet's children class object ".format(animal1))



        


# this is a special day for me, I have to remember it forever. 2025-01-27
#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2021/1/27 11:11
