# Project Euler Problem 40
# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.# # 

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000


target = 1000000

frac = ''

a = 1

while len(frac) <= target:
    frac = frac + str(a)
    a = a + 1

d = [0, 9, 99, 999, 9999, 99999, 999999]

answer = 1

for i in d:
    answer = answer * int(frac[i])

print(answer)