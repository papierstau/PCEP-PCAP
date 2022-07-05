# from os import strerror


# counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
# # print(counters)
# file_name = input("Enter the name of the file to analyze: ")
# try:
#     f = open(file_name, "rt", encoding="utf-8")
#     print(f)   
#     for line in f:
#         print(line)
#         for char in line:
#             # If it is a letter...
#             if char.isalpha():
#                 # ... we'll treat it as lower-case and update the appropriate counter.
#              counters[char.lower()] += 1
   
    
#     f.close()
#     # Let's output the counters.
#     for char in counters.keys():
#         cnt = counters[char]
#         if cnt > 0:
#             print(char, '->',cnt)
# except IOError as e:
#     print("I/O error occurred: ", strerror(e.errno))


from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of the file to analyze: ")
try:
    f = open(file_name, "rt")
    for line in f:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
    f.close()
    f = open(file_name + '.hist', 'wt')
    # Note: we've used lambda to access the directory's elements and set reverse to get a valid order.
    for char in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
        cnt = counters[char]
        if cnt > 0:
            f.write(char + ' -> ' + str(cnt) + '\n')
    f.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

