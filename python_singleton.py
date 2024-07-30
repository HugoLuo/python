# class Singleton:
#     __instance = None
#     name = "Hugo"

#     #re-write __new__()
#     def __new__(cls):
#         if cls.__instance is None:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
    
#     def show(self,n):
#         print("---------------->show",Singleton.name,n)

# s1 =Singleton()

# s2 =Singleton()
# print("s1 object is {}".format(s1))

# print("s2 object is {}".format(s2))
# print(s1.show(7))
# print(s2.show(10))



# class Singleton:
#     __instance = None
#     name = "Hugo"

#     def __new__(cls):
#         if cls.__instance is None:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
    
#     def show(self,num):
#         print("------->show",Singleton.name,num)

# s1=Singleton()
# s2=Singleton()
# print(s1)
# print(s2)

# print(s1.show(10))
# print(s2.show(100))




class Singleton:
    __instance = None
    name = "Hugo"

    # def __init__(self,num) -> None:
    #     self.__num=num

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    
    def show(self,num):
        print("------->",Singleton.name,num)

s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)

s1.show(20)
s2.show(100)
# s1.show