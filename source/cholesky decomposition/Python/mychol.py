import numpy as np
import time
from scipy.linalg import lu


def is_pos_def(x):
    if np.all(np.linalg.eigvals(x) > 0):
        print("yes")


def spd_matrix_generator(size):
    A = np.random.rand(int(size))
    A = A @ np.transpose(A)
    A = A + size * np.eye(size)
    return A


def my_lu():
    sizes = np.array([1024, 2048, 4096, 8192])
    times = np.array([0.0, 0.0, 0.0, 0.0])

    for i in range(4):
        matrix = spd_matrix_generator(sizes[i])
        start = time.time()
        L = np.linalg.cholesky(matrix)
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
    my_lu()
    i = i + 1
    print(str(i / 2) + '%')

