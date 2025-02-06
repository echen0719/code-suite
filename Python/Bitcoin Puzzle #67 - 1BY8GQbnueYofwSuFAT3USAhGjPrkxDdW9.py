import ecdsa
import hashlib
import base58
from numba import jit
import numpy as np

@jit(nopython=True)
def genNum():
    return np.random.rand()

def address_giver(key_int):
    sign_key = ecdsa.SigningKey.from_secret_exponent(key_int, curve=ecdsa.SECP256k1)
    public_key = sign_key.get_verifying_key().to_string("compressed")

    ripemd160 = b"\x00" + hashlib.new('ripemd160', hashlib.sha256(public_key).digest()).digest()
    checksum = hashlib.sha256(hashlib.sha256(ripemd160).digest()).digest()[:4]
    address = base58.b58encode(ripemd160 + checksum).decode("utf-8")

    return address

# 1. Generate private key between low, high + 1
# 2. Use address_giver to find address
# 3. Check if address is equal to reward wallet
# 4. Stop loop and save to file called found.txt (if found [which is never])

while True:
    i = int(genNum() * 73786976294838206465) + 73786976294838206464
    address = address_giver(i)
    print("{}. {}".format(i, address))

    if (address == "1BY8GQbnueYofwSuFAT3USAhGjPrkxDdW9"):
        with open("found.txt", "a") as file:
            file.write("{}. {} ({})".format(i, address, hex(i)))
        break

# generates a random int between 73786976294838206464 - 147573952589676412928 and takes the address

# I'll probably ask my friend to help me with C-family code

# pycoin --> address_giver: 1370 hashes/s --> 3450 hashes/s (151.8% increase)
# randint --> numpy: 3450 hashes/s --> 3840 hashes/s (11.3% increase)
