import matplotlib.pyplot as plt
import math
import random

x = []
y = []

# from [start, end] (inclusive)
def logger(base, start, end):
    for i in range(start, end + 1):
        x.append(i)
        y.append(math.log(i, base))
    plot()

def elliptic_curve(start, end, points):
    for _ in range(points):
        randX = random.uniform(start, end)
        x.append(randX)
        y.append((randX ** 3 + 7) ** 0.5)
        y.append(-1 * ((randX ** 3 + 7) ** 0.5))
    plot2()

def plot():
    plt.plot(x, y, 'bo')
    plt.show()

def plot2():
    for i in range(len(x)):
        plt.plot(x[i], y[i], 'bo')
        plt.plot(x[i], y[i+1], 'bo')
    plt.show()

#logger(10, 1, 100)
elliptic_curve(-2, 10, 100)