# Project Euler Problem 48
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def ChopTen(n):
    a = str(n)
    if len(a) <= 10:
        return a
    return a[-10:]

s = 0

for i in range(1,1001):
    print("Adding number: ", i, "^", i, end = "\r")
    n = ChopTen(i ** i)
    s = s + int(n)

print("\n\nLast 10 digits of sum: ", ChopTen(s))