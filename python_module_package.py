__all__ = [VAR1,OneClass]

print(">>>>>>>>>>>>>>>>")
print(__name__)
if __name__ == "__main__":
    print("As master running")


VAR1=1000

def onefunc():
    print("there are one func be invoke")

class OneClass:
    def funcInclass(self):
        print("func In class be invoke")