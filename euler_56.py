# Project Euler Problem 56
# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

def AddDigits(n):
    d = 0
    for i in str(n):
        d = d + int(i)
    return d

answer = 0

for a in range(1, 100):
    for b in range(1, 100):
        answer = max(answer, AddDigits(a ** b))

print("Maximum digital sum for a, b < 100:", answer)