# Project Euler Problem 77
# It is possible to write ten as the sum of primes in exactly five different ways:

# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2

# What is the first value which can be written as the sum of primes in over five thousand different ways?

import time

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

start = time.time()

primes = SieveOfEratosthenes(80)

limit = 5000
current = 11

found = False

while not found:
    ways_to_sum = [1] + [0] * current
    for p in primes:
        for i in range(p, current + 1):
            ways_to_sum[i] += ways_to_sum[i - p]
    if ways_to_sum[current] > limit:
        found = True
        break
    current += 1

end = time.time()
print("First sum to exceed", limit, ":", current)
print("Time taken:", end - start)
