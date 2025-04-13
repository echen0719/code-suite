import hashlib
import time
import random
import string

def hasher(beginning_zeros):
    prefix = '0' * beginning_zeros
    start = time.time()
    
    while True:
        random_int = random.randint(1, 128)
        hash_input = str(random.getrandbits(random_int))
        sha256_hash = hashlib.sha256(hash_input.encode()).hexdigest()
        
        if sha256_hash.startswith(prefix):
            end = time.time()
            time_taken = end - start
            print("Found hash: {} for input: {}".format(sha256_hash, hash_input)) # I'll try using Python 2.x formatting
            print("Time taken: {:.2f} seconds".format(time_taken))
            break

print("Current Bitcoin Difficulty - 19")
hasher(int(input("How many zeros?: ")))
