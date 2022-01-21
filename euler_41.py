# Project Euler Problem 41
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

import math
import sys
from itertools import permutations

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

def CheckIfPrime(n, l):
    for i in l:
        if n % i == 0:
            return False
    return True

target = 1000000000

p_list = SieveOfEratosthenes(int(math.sqrt(target)) + 1)

n = '987654321'

while len(n) != 0:
    a = permutations(n)
    for i in a:
        b = ''
        for j in i:
            b = b + j
        if CheckIfPrime(int(b), p_list):
            print("Found prime: ",b)
            sys.exit()
    n = n[1:]