text =(input("Type your Text Here "))
pal= ''



for char in text:
    if char.isspace():
        continue
    else:
        pal += char
        
str1 = pal[ :(len(pal)//2)]

str2 = pal[(len(pal)//2)+1: ]
for char in str2:
    str2

print(str2)
class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)

