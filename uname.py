# import platform

# print(platform.uname())

# import os

# returned_value = os.system("mkdir my_first_directory")
# print(returned_value)
# import time

# timestamp = 1572879180
# a = (time.gmtime(timestamp))
# print(time.localtime())
# print(a[8])
from datetime import datetime

print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())
from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d %z'))