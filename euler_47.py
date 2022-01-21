# Project Euler Problem 47
# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

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

def GetPrimeFactors(l, n):
    i = 0
    a = set()
    while l[i] < n / 2:
        if n % l[i] == 0:
            a.add(l[i])
        i = i + 1
    return a

def CheckFactors(a, b, c, d):
    l = [len(a), len(b), len(c), len(d)]
    s = []
    for i in range(1, 5):
        if l[i-1] < 4:
            s.append(i)
        else:
            s.append(0)
    return max(s)

target = 1000000

i = 646

p_list = SieveOfEratosthenes(target)

found = False

while not found:
    print("Testing numbers: ",i, i + 1, i + 2, i + 3, end = "\r")
    a, b, c, d = GetPrimeFactors(p_list, i), GetPrimeFactors(p_list, i + 1), GetPrimeFactors(p_list, i + 2), GetPrimeFactors(p_list, i + 3)
    n = CheckFactors(a, b, c, d)
    if n == 0:
        print("\n\nFound it! First number is ", i)
        found = True
    i = i + n