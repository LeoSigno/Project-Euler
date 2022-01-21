# Project Euler Problem 34
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

import math

def CheckFactorial(n):
    s = 0
    l = [int(i) for i in str(n)]
    for i in l:
        s = s + math.factorial(i)
    if s == n:
        return True
    return False

upper_bound = 2540160
facs = []

for i in range(3,upper_bound):
    if CheckFactorial(i):
        facs.append(i)

answer = 0

for i in facs:
    answer = answer + i

print(answer)