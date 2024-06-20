import sys
def sys_refcount():
    x = []

    print(sys.getrefcount(x))

    y = x 
    print("x refcount is :",sys.getrefcount(x))
    print("y refcount is :",sys.getrefcount(y))
    print("---------------------------")

    y=1
    print("x refcount is :",sys.getrefcount(x))
    print("y refcount is :",sys.getrefcount(y))

def div_number():
    print("5 / 2",5/2)
    print("5 // 2",5//2)
    print("5 % 2",5%2)
    print('divmod(5,2)=',divmod(5,2))





