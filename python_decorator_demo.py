def decorator(func):            #定义装饰器
    print("start decorator")
    def wrapper(*args,**kwargs):    #*args 表示接受可变参数   **kwargs 则表示接受接受包含关键字的参数。
        print("start wrapper")
        func(*args,**kwargs)
        print("end wrapper")
    print("decotrator1 will end")
    return wrapper    # 返回给被装饰的方法函数

@decorator   #使用装饰器，对方法函数f1 进行包装。
def f1(x):
    print("this is one function1 , initual , nothing")

@decorator
def f2(name,age):
    print("this is one function2")

@decorator
def f3(students,clazz='203'):
    print("{} 班有以下的学生".format(clazz))
    for student in students:
        print(student)




# f1(12)

# f2('Any',18)

# students=['Tom',"Jack","Hugo","Albert"]
# f3(students,clazz='9527')  #指定第二个参数
# f3(students)    #第二个参数使用默认值


def decorator2(func):
    print("start decorator2")
    def wrapper2(*args,**kwargs):
        print("start wrapper2")
        func(*args,**kwargs)
        print("end wrapper2")
    print("decotrator2 will end")
    return wrapper2

#对first_fun进行多层包装，decorator包装装饰完后的结果作为参数传给decorator2再进行包装装饰，以此类推。
#                       执行次序则是：越接近方法函数的装饰器越早被执行。
@decorator2
@decorator
def first_fun():
    print("this is first func")


first_fun()