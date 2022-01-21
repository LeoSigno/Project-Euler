# Project Euler Problem 35
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

import math

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

def CheckCircular(l,a):
    a = str(a)
    for i in range(len(a)):
        rotnum = a[i:]+a[:i]
        if int(rotnum) not in l:
            return False
    return True

big_n = 1000000

p_list = SieveOfEratosthenes(big_n)

answer = 0

for i in p_list:
    print("Checking Prime: ",i, end = "\r")
    if CheckCircular(p_list,i):
        answer = answer + 1

print("\n\nTotal Circular Primes: ",answer)