# Project Euler Problem 32
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from itertools import permutations

def CheckProduct(s):
    for i in range(1, 3):
        if int(s[:i]) * int(s[i:5]) == int(s[5:]):
            print("Solution found :",int(s[:i])," * ",int(s[i:5])," = ",int(s[5:]))
            return int(s[5:])
    return 0

a = '123456789'
perms = [''.join(p) for p in permutations(a)]

answer = set()

for i in perms:
    answer.add(CheckProduct(i))

print(sum(answer))