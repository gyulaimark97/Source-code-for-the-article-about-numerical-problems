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


def my_lu(size):
    matrix = spd_matrix_generator(size)

    start = time.time()
    p, l, u = lu(matrix)
    runtime = time.time() - start

    name = "result" + str(size) + ".txt"
    file = open(name, "a+")
    file.write(str(runtime))
    file.write('\n')
    file.close()


i = 0
while i < 200:
    my_lu(1024)
    i = i + 1
    print(i / 2)

i = 0
while i < 200:
    my_lu(2048)
    i = i + 1
    print(i / 2)

i = 0
while i < 200:
    my_lu(4096)
    i = i + 1
    print(i / 2)

i = 0
while i < 200:
    my_lu(8192)
    i = i + 1
    print(i / 2)
