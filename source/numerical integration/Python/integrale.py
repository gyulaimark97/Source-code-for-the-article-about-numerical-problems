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


def simpson (d, x, element_number):
    summ=0;
    for i in range (element_number-1):
        temp = ((x[i+1] - x[i])/6) * (d(x[i]) + 4* d((x[i]+ x[i+1])/2) + d(x[i+1]))
        summ = summ + temp
    return summ


def main():
    functions = [f, g, h, j]
    times = np.array([0.0, 0.0, 0.0, 0.0])
    x = np.linspace(0, 100, num=1000, endpoint=True)
    int_value=0;
    for i in range(4):
        start = time.time()
        int_value = simpson(functions[i], x, len(x))
        print(int_value)
        times[i] = time.time() - start

    name = "result.csv"
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

