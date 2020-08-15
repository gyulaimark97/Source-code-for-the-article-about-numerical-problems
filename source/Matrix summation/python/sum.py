import numpy as np
import time
import sys


def main(args):
    matrix1 = np.random.rand(int(args),int(args))
    matrix2 = np.random.rand(int(args), int(args))

    start = time.time()
    matrix3 = matrix1+matrix2
    generation_time = time.time() - start

    name = "result"+str(args)+".txt"
    file = open(name, "a+")
    file.write(str(generation_time))
    file.write('\n')
    file.close()

i = 0
while (i < 200):
    main(1024)
    i = i + 1
    print(i/2)

i=0
while (i < 200):
    main(2048)
    i = i + 1
    print(i / 2)

i = 0
while (i < 200):
    main(4096)
    i = i + 1
    print(i / 2)

i = 0
while (i < 200):
    main(8192)
    i = i + 1
    print(i / 2)