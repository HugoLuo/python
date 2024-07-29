# #
# g = (x*3 for x in range(100))
# print(type(g))
# print(g)

# print(g.__next__())
# print(g.__next__())

# print(next(g))
# print(next(g))


# while True:
#     try:
#         print(next(g))
#     except:
#         print("no more element")
#         break

# #define generator
# def gen():
#     i = 0
#     while 1 < 5:
#         temp = yield i 
#         print('temp:',temp)
#         for x in range(temp):
#             print('--------->')
#         print("**********")
#         i += 1
#     return "没有更多的数据"

# g = gen()



# print(next(g))
# print(next(g))

# print(g.send(None))
# n1 = g.send(3)
# print("n1=",n1)
# n2 = g.send(5)
# print("n2=",n2)





# def func():
#     n = 0 
#     while True:
#         n += 1
#         yield n
# g=func()
# print(g)


# def fib(length):
#     a, b = 0, 1
#     n = 0
#     while n < length:
#         yield b
#         a, b = b, a + b
#         n += 1

#     return '没有更多的元素'

# g=fib(8)

# print(next(g))
# print(next(g))

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# from typing import Any


# def fib2(length):
#     a, b = 0, 1
#     n = 0
#     while n<length:
#         yield b
#         a, b = b, b+a
#         n += 1
#     return "没有更多元素了"
# g2=fib2(10)
# print(g2.__next__())


import sys

class Person:

    # def __new__():
    #     print("method __new__() be call")

    # def __init__():
    #     print("method __init__() be called")

    # def __call__():
    #     print("method __call__() be called")
    
    # def __del__():
    #     print("method __del__()")

    @staticmethod
    def one_static_method():
        print("one statice method be call")

    @classmethod
    def one_class_method(cls):
        print("one class method be call")

    def one_common_method(self):
        print("one common method be call")

p=Person()
p.one_common_method()
Person.one_class_method()
Person.one_static_method()




    