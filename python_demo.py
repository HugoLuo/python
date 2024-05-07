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
sum_list([10,20,30])

