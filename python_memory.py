import sys
def sys_refcount():
    x = []

    print(sys.getrefcount(x))

    y = x 
    print("x refcount is :",sys.getrefcount(x))
    print("y refcount is :",sys.getrefcount(y))
    print("---------------------------")

    y=1
    print("x refcount is :",sys.getrefcount(x))
    print("y refcount is :",sys.getrefcount(y))

def div_number():
    print("5 / 2",5/2)
    print("5 // 2",5//2)
    print("5 % 2",5%2)
    print('divmod(5,2)=',divmod(5,2))


def if_statement():
    score = 80 
    #满足某一分支执行该分支的内容后，后面的分支将不再被执行。 
    if score >= 60:
        print("Good")
    elif score >100:
        print("too big")
    elif score < 0:
        print("too small ")

    if 0:
        print("0 is True")
    else:
        print("0 is False")
    if ():
        print("() is True")
    else:
        print("() is False")
    if []:
        print("[] is True")
    else:
        print("[] is False")    
    str1=""
    if str1:
        print('str1="" is True')
    else:
        print('str1="" is False')
    
    if None:
        print("None is True")
    else:
        print("None is Flase")
    
    if not None:
        print("not None is True")
    else:
        print("not None is Flase")
# if_statement()    


def max_number():
    num1=int(input("number1 is :"))
    num2=int(input("number2 is :"))
    if num1 > num2:
        print(num1,">",num2)
    elif num1 <= num2:
        if num1 < num2:
            print(num2,">",num1)
        else:
            print(num1,"=",num2)

max_number()




