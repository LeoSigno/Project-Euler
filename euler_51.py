# Project Euler Problem 51
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

from collections import Counter
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

def GenPrimeSubs(n):
    a = str(n)
    b = Counter(a)
    c = list(b.keys())[list(b.values()).index(3)]
    r = []
    for i in a:
        if i == c:
            r.append(1)
        else:
            r.append(0)
    l = []
    for i in range(10):
        s = ''
        for j in range(len(a)):
            if r[j] == 1:
                s = s + str(i)
            else:
                s = s + a[j]
        l.append(int(s))
    return l
    
        

target = 1000000

p_list = SieveOfEratosthenes(target)

print(16667 in p_list)

repeats = []

for i in p_list:
    c = Counter(str(i))
    if any(value == 3 for value in c.values()):
        repeats.append(i)

for i in repeats:
    l = GenPrimeSubs(i)
    print("Testing prime list ", l, end = "\r")
    answer = []
    if len(str(l[0])) != len(str(l[1])):
        l.remove(l[0])
    for j in l:
        if j in p_list:
            answer.append(j)
    if len(answer) == 8:
        print("\n\nFount it!")
        print(answer)
        sys.exit()