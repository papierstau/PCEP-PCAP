cipher = input("Enter line of text: ")

shiftValue = int(input("Enter shift value(1-25) "))

text = ''

try:
    if shiftValue > 0 and shiftValue <=25:
        print("shift value",shiftValue)
    else:
        print("not in range 1-25")
except:
    print("non valide number")

for char in cipher:
    if  char.isalpha():
        caesarShift = ord(char) + shiftValue
        # print("cS",caesarShift)
        if char.isupper():
            _helper = ord("A")
        elif char.islower():
            _helper = ord("a")
        
        caesar = (caesarShift - _helper) % 26
        # print("c",caesar)
        # print("_h",_helper)
        text += chr(_helper + caesar)
        
    else:
        text += char

print(text)

    

    