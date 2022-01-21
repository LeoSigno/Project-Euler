# Project Euler Problem 43
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

from itertools import permutations

def CheckProperty(l, n):
    a = str(n)
    for i in range(len(l)):
        b = int(''.join([str(a[i + 1]), str(a[i + 2]), str(a[i + 3])]))
        if b % l[i] != 0:
            return False
    return True

p_list = [2, 3, 5, 7, 11, 13, 17]

a = '0123456789'

b = permutations(a)

answer = set()

for i in b:
    if i[0] == '0':
        continue
    n = ''
    for j in i:
        n = n + j
    if CheckProperty(p_list, n):
        print("Found number: ",n, end = "\r")
        answer.add(int(n))

print("\n\nSum of numbers: ",sum(answer))