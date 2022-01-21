# Euler Project Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def checkDivisors(n):
    for i in range(19,10,-1):   #disregard divisors less than 11 because of common factors
        if n % i != 0:
            return False
    return True

a = 0

while True:
    a = a + 2520                #already know 2520 contains factors smaller than 11
    print("testing ",a,"\r")
    if checkDivisors(a):
        break

print("\nFound multiple: ",a)