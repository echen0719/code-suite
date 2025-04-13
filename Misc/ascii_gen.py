string = ""
MB = '0' * 1024 * 1024

length = int(input("How many characters (-1 to fill whole disk with 0s)? "))

if length >= 0:
      for i in range(length):
            string += chr(random.randint(32,126))
            with open("ASCII_String.txt", "w") as text:
                text.write(string)

if length == -1:
      while True:
            with open("junker", "a") as text:
                  text.write(MB)
