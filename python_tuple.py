def common_tuple():
    tuple1=(1,)
    print(type(tuple1))
    print(len(tuple1))
    print(tuple1[0])
    one_list=[2,3,4,5]
    v_1 = "one_str"
    tuple2=(1,one_list,6,7,8,v_1)
    print("tuple2 len is ",len(tuple2))
    print("tuple2 type is ",type(tuple2))
    print("print tuple2 ",tuple2)
    print("print tuple2[1] ", tuple2[1])
    tuple2[1][0]=20
    print("print tuple2[1] ", tuple2[1])
    tuple2[1][1]=100
    print("print tuple2[1] ", tuple2[1])
    one_list.append("add_one_str")
    print("print one_list ",one_list)
    print("print tuple2 len ",len(tuple2))
    print("print tuple2 ",tuple2)
    print("print tuple2[1] ",tuple2[1])
    print("print tuple2 last one is ",tuple2[-1])
    v_1 = 10000
    print("print tuple2 last one is ",tuple2[-1])
    print("print tuple2 last one type",type(tuple2[-1]))
    print("print tuple2[1] type",type(tuple2[1]))
    




common_tuple()


from collections import namedtuple
def namedtuple_demo():
    Student = namedtuple('S','name,age')
    s1 = Student('Hugo',42)
    print(s1)
    print(s1.name)
    print(s1.age)