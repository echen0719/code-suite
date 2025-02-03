import random
from pycoin.symbols.btc import network as solver # https://pypi.org/project/pycoin/

# 1. Generate private key between low, high + 1
# 2. Use pycoin to create address
# 3. Check if address is equal to reward wallet
# 4. Stop loop and save to file called found.txt

while True:
    i = random.randint(73786976294838206464, 147573952589676412928)
    private_key = solver.parse.secret_exponent(i).address()
    print("{}. {}".format(i, private_key))

    if (private_key == "1BY8GQbnueYofwSuFAT3USAhGjPrkxDdW9"):
        with open("found.txt", "a") as file:
            file.write("{}. {} ({})".format(i, private_key, hex(i)))
        break

# generates a random int between 73786976294838206464 - 147573952589676412928 and takes the address

# I'll probably ask my friend to help me with C-family code
