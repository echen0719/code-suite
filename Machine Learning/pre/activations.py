import math

X = [i/10 for i in range(-20, 21)]
for x in X:
    print('For value {}: '.format(x), end='')
    # sqrtSCurve = x / math.sqrt(1 + math.pow(x, 2))
    # tanh = (math.pow(math.e, x) - math.pow(math.e, -x))/(math.pow(math.e, x) + math.pow(math.e, -x))
    # print(sqrtSCurve, tanh)
    rationalCurve = 1 / math.pow(1 + math.pow(x, 2), 3)
    print(rationalCurve)
