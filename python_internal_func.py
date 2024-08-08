#there are some interal function, which we usage frequently.

#ord() 将送入的字母转化成ASCII编码
one_litter=ord("L")
print(one_litter)

#str() 将送入的参数，转变成字符串形式返回
s_type=str(123)
print(type(s_type))

#int() 将送入的参数，转变成
i_type=int('999')
print(type(i_type))

#pint() 这也系统内置的一个方法

#type() 对传入的参数

#isinstance() 看参数1 看是否是参数2类中的一个实例。  

result1=isinstance("ABc",str)
print(result1)

result2=isinstance("ABc",int)
print(result2)



m1 =100
m2 =200
m1,m2 = m2, m1
print(m1,m2)

m3,m4 = 300,400
m3,m4 = m4,m3
print(m3,m4)


import sys
astr = '今天你学习python了吗？'
size=sys.getsizeof(astr)
print("size = ",size)

newstr = astr[::-1]
print(newstr)

# astr = newstr*100
# print(astr)

astr = 'python happy'

print(astr.upper())
print(astr.capitalize())
print(astr.title())

def union(l1,l2):
    return list(set(l1+l2))

list1,list2 = [5,2,0],[2,3,5]
new_list=union(list1,list2)
print(new_list)