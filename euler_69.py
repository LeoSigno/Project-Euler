# Project Euler Problem 69
# Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

# n	Relatively Prime	φ(n)	n/φ(n)
# 2	    1	            1	    2
# 3	    1,2	            2	    1.5
# 4	    1,3	            2	    2
# 5	    1,2,3,4	        4	    1.25
# 6	    1,5	            2	    3
# 7	    1,2,3,4,5,6	    6	    1.1666...
# 8	    1,3,5,7	        4	    2
# 9	    1,2,4,5,7,8	    6	    1.5
# 10	1,3,7,9	        4	    2.5
# It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

import time
import math
start = time.time()

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

target = 200

limit = 1000000

answer = 1

p_list = SieveOfEratosthenes(target)

for i in p_list:
    if answer * i > limit:
        break
    answer = answer * i

print("Final n:", answer)
end = time.time()
print("Run time:", end - start)