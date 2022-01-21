# Project Euler Problem 80
# It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

# The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

# For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

import time
import math
from decimal import *

def getDigitsSum(string):
    string = string.replace('.','')
    total_sum = 0
    counter = 0
    for i in range(100):
        total_sum += int(string[i])
        counter += 1
    return total_sum

start = time.time()

limit = 100

answer = 0

getcontext().prec = 102 # Set precision to 101 decimal places to avoid rounding errors

n = [i for i in range(limit + 1)] # Initialize list of numbers

for i in range(int(limit ** 0.5) + 1): # Remove squares
    if i * i in n:
        n.remove(i * i)

for i in n:
    a = str(Decimal(i).sqrt())
    answer += getDigitsSum(a)

end = time.time()
print("Sum of 100 digits of first", limit, "irrational roots:", answer)
print("Time taken:", end - start)
