# Opening tzop.txt in read mode, returning it as a file object:
stream = open("test.txt", "rt", encoding = "utf-8")

print(stream.read()) # printing the content of the file
