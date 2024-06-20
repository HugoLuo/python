def list_demo():
    list1 =[1,3,5,6]
    print("list1 is ",list1)
    print("list1 type is ",type(list1))
    print("list1 len is ",len(list1))
    
    if isinstance(list1,list):
        print("list1 is instance of list")
    else:
        print("list1 NOT one instance of list")
    for item in list1:
        print("list ",item)

    # list pop
    # list1.pop(-1)
    for i in range(2):
        list1.pop(-1)
        print("after list.pop(-1) the list1 will be ",list1)
    # print("after list.pop(-1) the list1 will be ",list1)

    # list append
    list1.append('9527')
    print("after append 9527 the list1 is ",list1)

    # list update some one element
    list1[2]="update_element_one"
    print("list update the three element will be ",list1)

# list_demo()

from collections import namedtuple
def namedtuple_demo():
    Person = namedtuple("P","name,sex,age,address")
    p1 = Person('Hugo',1,42,"Canton Liwan")
    print("p1 is ", p1)
    print("p1 type of ",type(p1))

import math
def number_handle():
    print("math.floor 10.1 ", math.floor(10.1))
    print("math.floor 10.500000 ", math.floor(10.50000))
    print("math.floor 10.500001 ", math.floor(10.50001))
    print("math.floor 10.600001 ", math.floor(10.60001))
    print('------')
    print("math.ceil 10.1 ", math.ceil(10.1))
    print("math.ceil 10.500000 ", math.ceil(10.50000))
    print("------")
    print("round() 10.1 ", round(10.23))
    print("round() 10.500000 ", round(10.500000))
    print("round() 10.500001 ", round(10.500001))
    print("-------")
    print("10/3 = ",10/3)
    print("10//3 = ",10//3)
    print("10%3 = ",10%3)
    print("divmod(10,3) = ",divmod(10,3))
    print("10**2=",10**2)
    print("10**0.5=",10**0.5)
    print("9**0.5=",9**0.5)
    print("math.sqrt(8)=",math.sqrt(8))
  

# number_handle()

def list_define():
    l1=[]
    l2=list()
    l3=list(range(10))  
    print(l1,l2,l3)
    index_is=l3.index(1)
    print(index_is)
    l3.append("add_1")
    l3.append("add_2")
    print("l3 length is",len(l3))
    index_is=l3.index('add_1')
    print(index_is)

    # index_is=l3.index('add')
    # print(index_is)

    l3.append(1)
    print(" how many 1 in l3  ",l3.count(1))
    print(l3[-1])
# list_define()

import copy
def list_demo_dump():
    l1 = [1,2,3,4]
    l2 = l1
    print(l1,l2)
    l2[1]='b'
    print(l1,l2)

    l3=l2.copy()
    print(l1,l2,l3)
    l3[1]='b3'
    print(l1,l2,l3)

    l4 = l1 + l2
    print(l1,l2,l4)
    l5=l1
    # l5 = l1.extend(range(20))
    #extend  只是做个扩展成员的动作，其返回值是None, 类似Java的 void 
    l5.extend(("one","two","three"))
    print(l1,l3,l5)

    list1=['a',[1,2,3,4],'c','d'] 
    list2=list1.copy()
    print("list1=",list1," list2=",list2)
    list2[3]='D'
    print("list1=",list1," list2=",list2)
    list2[1][0]=100
    print("list1=",list1," list2=",list2)

    list3=copy.deepcopy(list1)
    list3[-1]='D3'
    list3[1][0]=1000
    print("list1=",list1," list3=",list3)
# list_demo_dump()

def list_demo3():
    list1=[1,2,3]
    list1.extend(range(3))
    list2 = list1
    list3 = copy.deepcopy(list1)
    print("list1's id is ",id(list1))
    print("list2's id is ",id(list2))
    print("list3's id is ",id(list3))
    print("list1=",list1)
    print("list2=",list2)
    flag0 = 2 in list1
    print("2 in list1 ? ",7.in(list1))
    print("2 in list1 ?",flag0)
    print("2's index list1 ",list1.index(2))
    list1.append("Tom")
    print("list1=",list1)
    print("Tom's index list1 ",list1.index('Tom'))
    flag= "Hugo" in list1 
    print("Tom in list1 ?",flag)
list_demo3()




