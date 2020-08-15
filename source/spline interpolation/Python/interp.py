import time
import numpy as np
from scipy import interpolate


def main():
    sizes = np.array([100000, 200000, 300000, 400000])
    times = np.array([0.0, 0.0, 0.0, 0.0])
    x = np.linspace(0, 30, num=30, endpoint=True)
    y = (x ** 3) / 4

    for i in range(4):
        xnew = np.linspace(0, 30, num=sizes[i], endpoint=True)
        results = np.zeros(sizes[i])
        start = time.time()
        tck = interpolate.splrep(x, y, s=0)
        ynew = interpolate.splev(xnew, tck, der=0)
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

