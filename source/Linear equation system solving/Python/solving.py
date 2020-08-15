import numpy as np
import random
import time


def is_pos_def(x):
    if np.all(np.linalg.eigvals(x) > 0):
        print("yes")


def spd_matrix_generator(n):
    A = np.random.randint(0, 10, (n, n))
    A = A @ np.transpose(A)
    A = A + n * np.eye(n)
    return A


def solving():
    sizes = np.array([512, 768, 1024, 1280])
    times = np.array([0.0, 0.0, 0.0, 0.0])

    for i in range(4):
        b = np.random.randint(0, 1000, (sizes[i]))
        matrix = spd_matrix_generator(sizes[i])
        start = time.time()
        x = np.linalg.solve(matrix, b)
        times[i] = time.time() - start

        ''' checking the results
        c = np.zeros(sizes[i])
        for j in range(sizes[i]):
            for k in range(sizes[i]):
                a=0
                c[j] = c[j] + matrix[j,k] * x[k]

        print(c)
        print(b)
        '''

    name = "result.csv"
    file = open(name, "a+")

    for i in range(4):
        file.write(str(times[i]))
        file.write(';')

    file.write('\n')
    file.close()


i = 0
while i < 200:
    solving()
    i = i + 1
    print(str(i / 2) + '%')

