temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 !=0:
        return True
    elif year % 400 !=0:
        return False
    else:
        return True
        
def days_in_month(year, month):
    year = is_year_leap(year)
    month31 = [1,3,5,7,8,10,12]
    
    for i in range(len(month31)):
        month_test = month31[i]
        if year == True and month == 2:
            return 29
        elif year != True and month ==2:
            return 28
        elif month == month_test:
            return 31
        else: 
            return 30

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")


my_tuple = (1, 10, 100, 1000)
my_tuple.__add__(555)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])


for elem in my_tuple:
    print(elem)
