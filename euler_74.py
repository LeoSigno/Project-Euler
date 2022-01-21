# Project Euler Problem 74
# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

# 1! + 4! + 5! = 1 + 24 + 120 = 145

# Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

# 169 → 363601 → 1454 → 169
# 871 → 45361 → 871
# 872 → 45362 → 872

# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

# 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
# 78 → 45360 → 871 → 45361 (→ 871)
# 540 → 145 (→ 145)

# Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

import time
import math
start = time.time()

def getFactorialSum(n):
    a = 0
    for d in str(n):
        a += math.factorial(int(d))
    return a

def getChainLength(n):
    l = [n]
    a = getFactorialSum(n)
    while a not in l:
        l.append(a)
        a = getFactorialSum(a)
    return len(l)
        
c = 0

limit = 1000000

for i in range(limit + 1):
    print("Checking chain lenght:", i, end = "\r")
    if getChainLength(i) == 60:
        c += 1

print("\n\nTotal number of 60 terms chains:", c)
end = time.time()
print("Run time:", end - start)