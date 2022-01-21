# Problem 30
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def CheckFifth(n):
    s = 0
    l = [int(i) for i in str(n)]
    for i in l:
        s = s + i**5
    if s == n:
        return True
    return False

upper_bound = 355000
fifths = []

for i in range(2,upper_bound):
    if CheckFifth(i):
        fifths.append(i)

answer = 0

for i in fifths:
    answer = answer + i

print(answer)