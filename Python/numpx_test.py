from numba import jit
import numpy as np

#init

@jit(nopython=True)
def genNum():
    random_number = np.random.randfloat(73786976294838206464, 147573952589676412929)
    print(random_number)

genNum()
