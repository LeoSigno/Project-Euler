# Project Euler Problem 62
# The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are cube.

import time
from itertools import permutations
start = time.time()
import sys

def BuildNumber(l):
    n = ''
    for i in l:
        n = n + i
    return int(n)

cubes = []

s = 345
t = 100000

for i in range(s, t):
    cubes.append(i ** 3)

d = {}

found = False

for i in cubes:
    k = int(''.join(sorted(str(i), reverse = True)))
    print("Testing cube:", i, "generated key:", k, end = "\r")
    if k not in d:
        d[k] = [1, i]
    else:
        d[k][0] = d[k][0] + 1
        if d[k][0] == 5:
            print("\n\nFound it! Smallest cube:", d[k][1])
            end = time.time()
            print("Run time:", end - start)
            sys.exit()