import time

islogin = False #默认是没有登陆的

#定义登陆函数
def login():
    username=input("Username is: ")
    password=input("Password is: ")
    if username == 'admin' and password == '123':
        return True
    else:
        return False

#定义一个装饰器，
def login_required(func):
    def wrapper(*args,**wkargs):
        global islogin 
        if islogin:
            func(*args,**wkargs)
        else:
            print("still no login,login first pls")
            #先去登陆吧。  
            # result = login()
            islogin = login()
            print("result is", islogin)
    return wrapper

#调用装饰器对支付函数进行功能(支付前看是否已经登陆)扩充
@login_required
def pay(money):
    print("paying ,free is {}".format(money))
    print("paying ......")
    time.sleep(2)
    print("finished pay ",money)

# print("the first time to pay ")
# pay(100)
# print("the second time to pay\n ************************")
# pay(200)

# print("the third time pay \n ************************")
# pay(300)


def about_memory():
    name1="Hugo"
    name2=name1
    name2="Boss"
    print(name1,id(name1))
    print(name1,id(name2))

about_memory()

help(input)