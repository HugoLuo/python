# Python Function

#print("hello,world")

def printlist():
    print("hello")


def myprint(name,city):
    print("我的名字是"+name)
    print("我所在的城市是:"+city)  

# myprint("Hugo","Guangzhou")
#myprint(name="zhangsan",city="hangzhou")

def print_name(*names):
    # print(names)
    for name in names:
        # print(name)
        print("name is {0}".format(name))
#print_name("Hugo","Jack",1,"date")

def print_info(**infor):
    # print(infor)
    for key,value in infor.items():
        print("key is {0}".format(key))
        print("value is {0}".format(value))

#print_info(name="hugo",age=3,city="Guangzhou")


def sum_list(mylist):
    result=0
    for onenumber in mylist:
        result = result + onenumber
    print(result)
#sum_list([10,20,30])


def checkage(age):
    if age > 0 and age < 120:
        return True
    else:
        return False
# age=10
# result =checkage(age)
# print(result)

number1=20
def local_variable_define():
    number1=3
    number2=7
    return number1*number2

# print(number1)
# result=local_variable_define()
# print(result)

def global_variable_define():
    global number1
    number1=100

# global_variable_define()
# print(number1)


def variable_define():
    global number1
    number1 = 2
    number2 = 7
    return number1*number2

# number1=1
# result=variable_define()
# print(result)
# print(number1)


