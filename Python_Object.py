# # Python Object

# name="Hugo"
# age=42
# # print("name is "+name+" Age is "+age)
# print("name is {0} age is {1}".format(name,age))

#define class
class MyPeople:
    name="hugo"
    age=42
    def print_info(self):
        print("My name is {0} and age is {1}".format(self.name,self.age))


# #instance class
# oneObject=MyPeople()
# oneObject.name="boss"
# oneObject.age=25
# oneObject.print_info()


class Person:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def print_info(self):
        print("My name is {0} and age is {1}".format(self.name,self.age))

obj=Person("Jon",23)
obj.print_info()