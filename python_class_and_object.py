
class Person:

    #魔术方法，为创建对象向系统申请内存资源，在创建一个新对象时调用，调用为了开辟空间返回将给__init__方法使用
    def __new__(cls, *args, **kwargs):
        print("--->__new__")
        return object.__new__(cls)

    #魔术方法,类似Java中的构造方法，在对象被初始化时被调用。
    def __init__(self, name1):
        self.name = name1
        print("--->__init__")

    def __call__():
        print("--->__call__")
        

    #魔术方法，重写该方法后，当打印对象时返回对应的内容，而非对象的地址。
    def __str__(self) -> str:
        return "this object's name is {}".format(self.name)

    


p = Person("Hugo")
# print(sys.refercount(p1))
print(p)

