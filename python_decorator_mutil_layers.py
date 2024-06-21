def decorator1(func):
    print("start decorater1")
    def wrapper1(*args,**kwargs):
        func(*args,**kwargs)
        print("do wrapper1 .....")
    print("decorator1 will end")
    return wrapper1


def decorator2(func):
    print("start decorator2")
    def wrapper2(*args,**kwargs):
        func(*args,**kwargs)
        print("do wrapper2")
    print("decotrator2 will end")
    return wrapper2

#对first_fun进行多层包装，decorator包装装饰完后的结果作为参数传给decorator2再进行包装装饰，以此类推。
#                       执行次序则是：越接近方法函数的装饰器越早被执行。
@decorator2
@decorator1
def first_fun():
    print("this is first func")

first_fun()

