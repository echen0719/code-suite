import ecdsa
import hashlib
import base58

def address_giver(key_int):
    # https://privatekeys.pw/calc

    sign_key = ecdsa.SigningKey.from_secret_exponent(key_int, curve=ecdsa.SECP256k1)
    public_key = (sign_key.get_verifying_key().to_string("compressed")).hex() # something with converty decimal to a public key

    # learning about how btc works and spending 5 hours on researching and coding this blew my mind
    public_key_bytes = bytes.fromhex(public_key)
    # takes sha256 of public key, then ripemd-160 on that output and appends "00"
    ripemd160 = "00" + hashlib.new('ripemd160', hashlib.sha256(public_key_bytes).digest()).hexdigest() # what is ripemd-160?
    checksum = (hashlib.sha256(hashlib.sha256(bytes.fromhex(ripemd160)).digest())).hexdigest() # does double sha256 on ripemd160
    address = base58.b58encode(bytes.fromhex(ripemd160) + bytes.fromhex(checksum[:8])).decode("utf-8")
    # encodes using b58 of ripemd160 and last 8 characters of checksum

    # https://i.sstatic.net/AcXYt.png

    print(address)

address_giver(102987336249554097029535212322581322789799900648198034993379397001115665086549)
