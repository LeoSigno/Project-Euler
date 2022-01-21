# Project Euler Problem 37
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import math
from itertools import product

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

def BuildCandidate(l,r,d):
    a = []
    a.append(l)
    for i in d:
        a.append(i)
    a.append(r)
    answer = ''
    for i in a:
        answer = answer + str(i)
    return int(answer)

def CheckTruncPrime(l,n):
    s = str(n)
    for i in range(len(s)):
        if int(s[i:]) not in l:
            return False
        if int(s[:i+1]) not in l:
            return False
    return True

target = 1000000

primes = SieveOfEratosthenes(target)

end_r = [2, 3, 5, 7]
end_l = [2, 3, 5, 7]
mid_d = [1, 3, 7, 9]

size = 2

trunc = set()

while size < 7:
    for l in end_l:
        for r in end_r:
            if size == 2:
                d = []
                p = BuildCandidate(l,r,d)
                print("Testing number: ",p, end = "\r")
                if CheckTruncPrime(primes,p):
                    print("\nFound truncated prime: ",p, end = "\n")
                    trunc.add(p)
            if size > 2:                
                m = product(mid_d, repeat = (size - 2))
                for d in m:
                    print("Testing number: ",p, end = "\r")
                    p = BuildCandidate(l,r,d)
                    if CheckTruncPrime(primes,p):
                        print("Found truncated prime: ",p, end = "\r")
                        trunc.add(p)
    size = size + 1

print("\n\nList of trucated primes: ", trunc)
print("\n\nSum of trucated primes: ", sum(trunc))