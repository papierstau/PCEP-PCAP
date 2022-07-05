dictionary = {'one':'2','3':'one', '2':'3'}
v = dictionary['one']

for k in range(len(dictionary)):
    v = dictionary[v]
print(v)

tup =(1,2,3,4,8)
tup = tup[1:-1]
tup = tup[0]
print(tup)
