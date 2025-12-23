print('LinesToArray - This program will take lines of text and create an array for you. To use, following the instruction below.\n')
print("Write or paste your text. Press Enter (sometimes twice) on an empty line to finish.")

# I tried appends and it didn't seem to work for me so extend is used instead
# This function will split words on separate lines or separated by spaces

def createArray():
    lines = []
    while True:
        line = input()
        if not line: break # breaks when user sends a blank line
        lines.extend(line.split())
    return lines

def returnJavaHashMap(lines):
    variableName = input('What is the hashmap variable name? ')
    hashmap = ''
    for line in lines:
        # I will worry about custom format another day
        hashmap += '{}.put("{}", {});\n'.format(variableName, line, 0.0)
    return hashmap
    
def returnPythonList(lines):
    return lines

# print("Your array is here:", returnJavaHashMap(createArray()))
print("Your array is here:", returnPythonList(createArray()))
