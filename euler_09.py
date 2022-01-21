# Project Euler Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import sys

def tripCalc(n):
    a = n
    b = int((1000-a)/2)
    c = 1000 - a - b
    return a,b,c

def checkPitagoras(a,b,c):
    if a*a + b*b == c*c:
        return True
    else:
        return False

for i in range(1,333,1):
    a,b,c = tripCalc(i)
    while a < b:
        if checkPitagoras(a,b,c):
            print("Winning triplet: ",a,b,c)
            print("Product: ",a*b*c)
            sys.exit()
        b = b - 1
        c = c + 1