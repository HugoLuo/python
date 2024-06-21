def decorator1(func):            #定义装饰器
    print("start decorator")
    def wrapper(*args,**kwargs):    #*args 表示接受可变参数   **kwargs 则表示接受接受包含关键字的参数。
        print("start wrapper")
        func(*args,**kwargs)
        print("end wrapper")
    print("decotrator1 will end")
    return wrapper    # 返回给被装饰的方法函数

@decorator1   #使用装饰器，对方法函数f1 进行包装。
def f1(x):
    print("this is one function1 , initual , nothing")

@decorator1
def f2(name,age):
    print("this is one function2")

@decorator1
def f3(students,clazz='203'):
    print("{} 班有以下的学生".format(clazz))
    for student in students:
        print(student)




f1(12)

f2('Any',18)

students=['Tom',"Jack","Hugo","Albert"]
f3(students,clazz='9527')  #指定第二个参数
f3(students)    #第二个参数使用默认值







