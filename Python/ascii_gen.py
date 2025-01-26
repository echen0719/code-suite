import random

string = ""

length = int(input("How many characters? "))

for i in range(length): 
   string += chr(random.randint(0,127))

print(string)
with open("ASCII_String.txt", "w") as text:
    text.write(string)
