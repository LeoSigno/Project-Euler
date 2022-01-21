# Project Euler Problem 53 
# There are exactly ten ways of selecting three from five, 12345:

# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# In combinatorics, we use the notation, 5C3 = 10.

# In general, ^nC_r = \frac{n!}{r!(n-r)!}

# where  r \leq n, n! = n\cdot (n-1)\cdot \dots \cdot 3 \cdot 2\cdot 1 and 0! = 1

# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

# How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

import math
import sys

answer = 0

for n in range(1, 101):
    for r in range(1, n + 1):
        print("Testing pair n =", n, "r =", r, end = "\r")
        if math.factorial(n) / (math.factorial(r) * math.factorial(n - r)) > 1000000:
            answer = answer + 1

print("\n\nCombination numbers larger than one million: ", answer)
