# Project Euler Problem 66
# Consider quadratic Diophantine equations of the form:

# x^2 – Dy^2 = 1

# For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

# It can be assumed that there are no solutions in positive integers when D is square.

# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

# 3^2 – 2×2^2 = 1
# 2^2 – 3×1^2 = 1
# 9^2 – 5×4^2 = 1
# 5^2 – 6×2^2 = 1
# 8^2 – 7×3^2 = 1

# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

import time
from math import sqrt
start = time.time()

def SolveDiophantine(n):
    x = 1
    solved = False
    while not solved:
        y = 1
        while x ** 2 > n * y ** 2:
            if x ** 2 - n * y ** 2 == 1:
                solved = True
            y = y + 1
        x = x + 1
    return x
    

target = 7

d = [i for i in range(1, target + 1)]

for i in range(1, int(target ** 0.5) + 1):
    d.remove(i ** 2)

s = []

for i in d:
    print("Solving Diophantine for D =", i, end = "\r")
    s.append(SolveDiophantine(i))
    
print("\n\nLargest x:", max(s), "corresponding D:", d[s.index(max(s))])

end = time.time()
print("Run time:", end - start)