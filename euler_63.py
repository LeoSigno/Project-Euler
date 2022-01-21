# Project Euler Problem 63
# The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

import time
from itertools import permutations
start = time.time()
import sys

c = 0

for i in range(1, 10):
    p = 1
    while True:
        if p == len(str(i ** p)):
            c = c + 1
        else:
            break
        p = p + 1

print("Total number of powerful integers:", c)

end = time.time()
print("Run time:", end - start)