# Project Euler Problem 16
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

a = 2**1000

b = [int(i) for i in str(a)]

answer = 0

for i in b:
    answer = answer + i

print("Total sum of digits: ",answer)