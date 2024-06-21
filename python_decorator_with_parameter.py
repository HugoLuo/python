#定义可以传参数的装饰器
def outer(p1):
    def decorator(func):
        def wrapper(*args,**kwargs):
            func(*args,**kwargs)
            print("传入装饰器的参数是 {}".format(p1))
        
        return wrapper
    return decorator

@outer(10)
def house1():
    print("这是第一间房子")

@outer(100)
def house2():
    print("这是第二间房子")


house1()

print("********")

house2()





# #定义带参数的装饰器
# def outer(p1):
#     def decorator3(func):
#         def wrapper2(*args,**kwwargs):
#             print("wrapper be call")
#             func()
#             print("我的房子有{}平方".format(p1))
#         return wrapper2
#     return decorator3

# import time
# #调用带参数的装饰器对new_house函数进行装饰
# @outer(10)
# def new_house():
#     print("我{}拿到房子的钥匙".format(time))

# @outer(100)
# def another_house():
#     print("另一间新房子在天河区")

# new_house()


# another_house()


