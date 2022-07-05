def outer(par):
    loc = par

    def inner():
        return loc
        
    return inner


var = 1
fun = outer(var)
print(fun())

b = bytearray(3)
print(b)

import calendar

print(calendar.weekheader(2))

import os
