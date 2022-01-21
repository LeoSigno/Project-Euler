# Project Euler Problem 49
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

from itertools import permutations
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

floor = 1000
ceiling = 10000

p_list = SieveOfEratosthenes(ceiling)

for i in range(len(p_list)):
    if p_list[i] > floor:
        p_list = p_list[i:]
        break

perms = []

for i in p_list:
    a = permutations(str(i))
    b = []
    for i in a:
        c = int(''.join(i))
        if c in p_list:
            b.append(c)
            p_list.remove(c)
    b.sort()
    if len(b) >= 3:
        perms.append(b)

s = []

for i in perms:
    for j in range(len(i) - 2):
        for k in range(1, len(i) - 1):
            for l in range(k, len(i)):
                if ((i[j] + i[l]) / 2 == i[k]) and (i[j] != i[l]):
                    s.append([i[j], i[k], i[l]])

print("Found solutions: ", s)

for i in s:
    a = ''
    for j in i:
        a = a + str(j)
    print(a)