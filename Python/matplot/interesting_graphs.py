import matplotlib.pyplot as plt
import math
import random

x = []
y = []

# from [start, end] (inclusive)
def logger(base, start, end):
    if (start < 0 or end < 0):
        print("Error! Logs can't start as a negative!")
        return
    if (base < 0):
        print("Error! Log bases have to be zero or greater!")
        return
    inc = start
    while inc <= end:
        plt.plot(inc, math.log(inc, base), '.')
        inc += 0.1
    plt.show()

# I just realized that overloading functions doesn't exist

def elliptic_curve(start, end, points):
    if (start < -1.912931):
        print("Error! SECP256K1's minimum X value is around -1.912931.")
        return
    for _ in range(points):
        randX = random.uniform(start, end)
        plt.plot(randX, (randX ** 3 + 7) ** 0.5, 'bo')
        plt.plot(randX, -1 * ((randX ** 3 + 7) ** 0.5), 'bo')
    plt.show()

logger(10, 1, 100)
#elliptic_curve(-1.91, 10, 1000)
