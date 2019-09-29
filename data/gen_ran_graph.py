""" Generate random graph
"""

import random
import numpy.random as nprnd


def main():
    # Erdos-renyi random graph
    n = 100
    p = 0.6
    print random.random()
    for i in range(1, n):
        line = str(i) + '\t'
        for j in range(1, n):
            if random.random() >= p and i != j:
                line += str(j) + '\t'
        print line
    line = str(1)
    if random.random() >= p:
        line


if __name__ == '__main__':
    main()
