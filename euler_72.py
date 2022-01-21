# Project Euler Problem 72
# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

# It can be seen that there are 21 elements in this set.

# How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

import time
import math
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

def getTotients(n):
    a = n
    factors = []
    i = 0
    while n > 1:
        p = p_list[i]
        if n % p == 0:
            factors.append(p)
            while math.ceil(n / p) == math.floor(n / p):
                n = n // p
        i += 1
    for t in factors:
        a *= 1 - (1 / t)
    return(int(a))

limit = 1000000

p_list = SieveOfEratosthenes(limit)

c = 0

for i in range(2, limit + 1):
    print("Testing denominator: ", i, end = "\r")
    c = c + getTotients(i)

print("\n\nTotal number of reduced proper fractions:", c)
end = time.time()
print("Run time:", end - start)