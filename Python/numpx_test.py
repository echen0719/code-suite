from numba import jit
import numpy as np

@jit(nopython=True)
def genNum():
    return np.random.rand()

#  861,000 integers per second

while True:
    i = int(genNum() * 73786976294838206465) + 73786976294838206464
    print(i)
