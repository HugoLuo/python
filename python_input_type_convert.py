
# 读取用户的输入，默认是接受字符串类型的
# result=input18
("Please input your result:")
# print(result)

# 不断接受用户的输入
# while True:
#     result=input("Pleae provide your input(type exit end session):")
#     if result == 'exit':
#         break


# 数值与字符串间的转换
str_age=input("Please provide your age:")
print(type(str_age))
age=int(str_age)
print(type(age))
print(age)

number=18
print(number)
print(type(number))
str_number=str(number)
print(type(str_number))

import sys
x = []
print(sys.getrefcount(x))