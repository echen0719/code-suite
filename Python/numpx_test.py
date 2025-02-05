from numba import jit
import numpy as np

np.set_printoptions(suppress=True)

@jit(nopython=True)
def genNum():
    return np.random.rand()

i = int(genNum() * 73786976294838206464 + 147573952589676412929)
print(i)
