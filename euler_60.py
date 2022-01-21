# Project Euler Problem 60
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

import math
import bisect
import time

start = time.time()

def FindClosestIndex(l, n):
    i = bisect.bisect_left(l, n)
    if i >= len(l):
        i = len(l) - 1
    elif i and l[i] - n > n - l[i - 1]:
        i = i - 1
    return (i)

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

def CheckPrime(n):
    t = FindClosestIndex(p_list, int(n ** 0.5))
    for i in range(t):
        if n % p_list[i] == 0:
            return False
    return True


def CheckConcPrime(a, b):
    if CheckPrime(int(str(a) + str(b))) and CheckPrime(int(str(b) + str(a))):
        return True
    return False

def TrailDict(n, d):
    for i in d[n]:
        nx = i
        a = [n, nx]
        s = set(d[n]).intersection(set(d[nx]))
        while len(s) != 0:
            nx = min(s)
            a.append(nx)
            s = s.intersection(set(d[nx]))
        if len(a) == 5:
            return a
    return 0

target = 10000

p_list = SieveOfEratosthenes(target)

d = {}

for i in range(len(p_list)):
    l = []
    for j in range(i + 1, len(p_list)):
        print("Testing primes: ", p_list[i], p_list[j], end = "\r")
        if CheckConcPrime(p_list[i], p_list[j]):
            l.append(p_list[j])
    d[p_list[i]] = l

answer = target * 4

for i in d:
    a = TrailDict(i, d)
    print("Testing prime:", i, "Chain:", a, end = "\r")
    if a != 0:
        answer = min(answer, sum(a))
        print("\nSolution found!",a , "Current Minimum:", answer, end = "\n")

print("\n\nLowest sum: ", answer)

end = time.time()

print("Total run time: ", end - start)