# Project Euler Problem 36
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def CheckPalindrome(n):
    a = str(n)
    for i in range(int(len(a)/2)):
        if a[i] != a[-(i+1)]:
            return False
    return True

target = 1000000

answer = 0

for i in range(target):
    b = format(i, 'b')
    if CheckPalindrome(i) and CheckPalindrome(b):
        answer = answer + i

print("Total sum of palindromes in base 10 and 2: ",answer)