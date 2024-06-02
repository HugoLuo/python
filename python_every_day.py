
# 2024-5-22 
# 找到最小的那个数字并输出
def min_number():
    number1=int(input("Please enter the first number:"))
    number2=int(input("Please enter the second number:"))
    number3=int(input("Please enter the third number:"))
    if number1 <= number2 and number1 <= number3:
        min_number = number1
    elif number2 <= number1 and number2 <= number3:
        min_number = number2
    else:
        min_number = number3

    print("最小的数字是：%d" %min_number)

# min_number()

def directory_key_and_value():
    data={1:"a",2:"b",3:"c"}
    if "a" in data:  #data 其实就是 data.key()  若想对value 进行查询 ,可用data.values()
        print("a")
    elif "3" in data:
        print("c")
    else:
        print("fail")

    if "a" in data.values():
        print("search by value can find a")
    if 2 in data.keys():
        print("search by key ,can find it<---2 ")
# directory_key_and_value()


def compute():
    a = 100
    b = 0 
    if a > 1:
        a //= 2
        b += 1
    print(a)
    print(b)
# compute()

def list_end_index():
    lists = [1,2,3,]
    a = lists.pop()
    print(a)
# list_end_index()

def type_trans_compare():
    a = float("inf")
    b = a+1
    print(a==b,b-a,b>a)
# type_trans_compare()

def string_index():
    string1="Hello world!"
    a = string1.index("o",5)
    print(a)
# string_index()

def func_list1():
    list1 = [[1,2,3],[4,5,6],[7,8,9]]
    # items = []
    # for item in list1:
    #     for i in item:
    #         items.append(i)
    # OR
    items=[i for item in list1 for i in item]

    print(items)
# func_list1()

def func_list2(lists,items=None):
    if items is None:
        items = []
    for item in lists:
        if type(item) != list:
            items.append(item)
        else:
            func_list2(item,items)
    return items

# res = func_list2([[1,2,3],[4,5],[[7,8,9]]])
# print(res)

def func_list3():
    lists = [True,False,0,None,1]
    result = lists[-1] or lists[0] and lists[2]  #and的优先级高于or, 不是从左到右来进行逻辑运算
    #  上面分成左右两部分： lists[-1]  和 （lists[0] and lists[2]）
    # 左边是1 , 而且后面是or ,就不管右手部分是什么逻辑运算结果，最终的结果就是1    
    print(result)

# func_list3()

import time
def progress():
    for i in range(11):
        progress = "#"*i + "-"*(10-i)
        print(f"r\033[1:32m{progress}",end="")
        time.sleep(0.5)

progress()