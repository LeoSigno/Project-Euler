# Project Euler Problem 27
# Euler published the remarkable quadratic formula:

# n² + n + 41

# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

# Using computers, the incredible formula  n² – 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

# Considering quadratics of the form:

# n² + an + b, where |a| < 1000 and |b| < 1000
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

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


def Streak(l,a,b):
    n = 0
    while (n**2 + n*a + b) in l:
        n = n + 1
    return n

b_l = SieveOfEratosthenes(1000)
for i in range(len(b_l)):
    b_l.append(-b_l[i])

b_l.sort()

p = SieveOfEratosthenes(1000000)

answer = 0
coefs = [0,0]

for a in range(-999,1000):
    for b in b_l:
        c = Streak(p,a,b)
        if c > answer:
            answer = max(answer, c)
            coefs = [a,b]
        print("Testing factors",a,"and",b,", current best streak from ",coefs,"    ", end = "\r")

print("\n\nProduct of coefficients: ",coefs[0]*coefs[1])