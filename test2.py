import math

try: 
    print(math.pow(2))
except TypeError:
    print("A")
else:
    print("b")


class A:
    def __init__(self,v ):
        self.__a = v +1
a = A(0)
print (a.__dict__)