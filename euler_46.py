# Project Euler Problem 46
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import math
import sys

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

def CheckProperty(l, n):
    i = 0
    while n > l[i]:
        if (((n - l[i]) / 2) ** 0.5) % 1 == 0:
            return True
        i = i + 1
    return False

target = 1000000

i = 33

p_list = SieveOfEratosthenes(target)

for j in range(i, target, 2):
    if j in p_list:
        continue
    print("Testing number: ", j, end = "\r")
    if not CheckProperty(p_list, j):
        print("\n\nFound it! Answer: ", j)
        sys.exit()