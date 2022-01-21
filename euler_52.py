# Project Euler Problem 52
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

from collections import Counter
import math
import sys

def CheckDigits(n):
    for i in range(2, 7):
        if Counter(str(n)) != Counter(str(n * i)):
            return False
    return True

n = 10

found = False

while not found:
    print("Testing number: ", n, end = "\r")
    if len(str(n)) != len(str(n * 6)):
        n = n + 1
        continue
    if CheckDigits(n):
        print("\n\nFound it!", n)
        found = True
    n = n + 1