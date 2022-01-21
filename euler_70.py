# Project Euler Problem 70
# Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
# The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

# Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

# Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

import time
import math
from itertools import combinations
start = time.time()

def SieveOfEratosthenes(n):
     
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    p_list = []
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Make prime list
    for p in range(n + 1):
        if prime[p]:
            p_list.append(p)
    return p_list

target = 10 ** 7

pairs = combinations(SieveOfEratosthenes(2 * int(target ** 0.5)), 2)
answer = (100, 0)
for n, t in ((a * b, (a-1) * (b-1)) for a, b in pairs if a * b < target):
    ratio = float(n) / t
    if ratio < answer[0] and sorted(str(n)) == sorted(str(t)):
        answer = (ratio, n)


print("Final n:", answer)
end = time.time()
print("Run time:", end - start)