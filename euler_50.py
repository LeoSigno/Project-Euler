# Project Euler Problem 50
# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

target = 1000000

p_list = SieveOfEratosthenes(target)

p_sum = []

a = len(p_list)

s = 0

for i in range(a):
    p_sum.append(s)
    s = s + p_list[i]
    print("Calculating sum list, current position: ", i, "/", a, end = "\r")

print("\n")
s = 0
limit = 0

while s < target:
    s = p_sum[limit]
    limit = limit + 1
    
for i in range(limit, 20, -1):
    for j in range(len(p_sum) - i):
        r = p_sum[j + i -1] - p_sum[j]
        print("Testing sum, length: ", i, "Prime Candidate: ", r, end = "\r")
        if r > target:
            break
        if r in p_list:
            print("\n\nFound it! Longest chain: ", i, ", prime: ", r)
            sys.exit()