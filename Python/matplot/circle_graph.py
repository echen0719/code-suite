import random
import matplotlib.pyplot as plt

x = []
y_top = []
y_bottom = []

for _ in range(10000):
    randX = random.uniform(-1, 1) # seems like uniform gives [-1, 1]
    x.append(randX)

    # x^2 + y^2 = 1 --> y^2 = 1 - x^2 --> y = +- sqrt(1 - x^2)
    solY = (1 - randX ** 2) ** 0.5
    solY2 = -(1 - randX ** 2) ** 0.5

    y_top.append(solY) # top of circle
    y_bottom.append(solY2) # bottom of circle

for i in range(len(x)):
    plt.plot(x[i], y_top[i], 'bo') # blue dots

for i in range(len(x)):
    plt.plot(x[i], y_bottom[i], 'bo') # more blue dots

plt.show()