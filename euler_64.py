# Project Euler Problem 64
# All square roots are periodic when written as continued fractions and can be written in the form:

# For example, let us consider 
 
# If we continue we would get the following expansion:

# The process can be summarised as follows:
# It can be seen that the sequence is repeating. For conciseness, we use the notation , to indicate that the block (1,3,1,8) repeats indefinitely.

# The first ten continued fraction representations of (irrational) square roots are:

# Exactly four continued fractions, for N <= 13, have an odd period.

# How many continued fractions for N <= 10000 have an odd period?

import time
from math import sqrt
start = time.time()

def CheckFraction(n):
    m = 0.0
    d = 1.0
    a0 = int(sqrt(n))
    an = int(sqrt(n))
    p = 0
    if a0 != sqrt(n):
        while an != 2 * a0:
            m = d * an - m
            d = (n - m ** 2) / d
            an = int((a0 + m) / d)
            p = p + 1
    return p

c = 0

for i in range(10000):
    if CheckFraction(i) % 2 != 0:
        c = c + 1

print("Odd period continued fractions below 10000:", c)
end = time.time()
print("Run time:", end - start)