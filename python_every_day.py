
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

