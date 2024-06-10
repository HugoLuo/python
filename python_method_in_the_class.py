
class Person:
    #there are one common function in class
    def one_common_func(self):
        print("this is one common function")
    
    @classmethod
    def class_method(cls):
        print("this is one classmethod in class")

    @staticmethod
    def static_method():
        print("this one static method in class")
    
    

#对象访问类中的上面的三种方法
print("Object access the methods")
Person.one_common_func(Person())
p1 = Person()
p1.one_common_func()
Person.class_method()
p1.class_method()
p1.static_method()
print("-------------------------")

#类访问各种方法
print("Class access the methods")
Person.one_common_func(Person())
Person.class_method()
Person.static_method()
print("-------------------------")




