import time

import numpy as np
from numpy import linalg as LA


def main():
    sizes = np.array([512, 1024, 1536, 2048])
    times = np.array([0.0, 0.0, 0.0, 0.0])

    for i in range(4):
        A = np.random.rand(sizes[i], sizes[i])
        start = time.time()
        w, v = LA.eig(A)
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

