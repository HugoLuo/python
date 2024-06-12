
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

# max_number()

def guess_input():
    num=12345
    if num >= 10000:
        print(">5")
    elif num >= 1000:
        print(" >4")
    elif num >=100:
        print(">3")
    elif num >10:
        print(" > 2")
    else:
        print(" >1")


from collections import namedtuple

Student = namedtuple('S','name,age')
s1 = Student("hugo",20)
print(s1)


