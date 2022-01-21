# Project Euler Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def checkPalindrome(n):
    a = str(n)
    b = int(len(a)/2)
    l = list(a)
    for i in range(b):
        if l[i] != l[-(i+1)]:
            return False
    return True

a = list(range(999,99,-1))

for i in a:
    b = i
    while b < 1000:
        c = b*i
        if checkPalindrome(c):
            print(c)
            break
        b = b+1