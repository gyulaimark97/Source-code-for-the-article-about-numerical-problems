import time
import numpy as np
import math
from scipy import interpolate

def f(x):
    return math.cos(x**3)-1


def g(x):
    return x**2 + x**3 + 3


def h(x):
    return math.sin(x)**2 + 3*x + 5 + math.tan(x+2)


def j(x):
    return math.sin(x**20 + x**30 + 3)**4 + 31*x + 6 * x**12


def firstderivate (d, x, step):
    return (d(x + step) - d(x - step)) / 2*step


def secondderivate (d, x, step):
    return (d(x + step) - 2*d(x) + d(x - step)) / step*step



def main():
    functions = [f, g, h, j]
    times = np.array([0.0, 0.0, 0.0, 0.0])
    x = np.linspace(0, 100, num=1000, endpoint=True)
    step = 100/1000
    der = np.zeros(1000)

    for i in range(4):
        start = time.time()
        t = 0
        while t < 1000:
            der[t] = secondderivate(functions[i], x[t], step)
            t = t + 1

        times[i] = time.time() - start

    name = "result2nd.csv"
    file = open(name, "a+")
    for i in range(4):
        file.write(str(times[i]))
        file.write(';')

    file.write('\n')
    file.close()


i = 0
while i < 200:
    main()
    i = i + 1
    print(str(i / 2) + '%')

