# Project Euler Problem 39
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

from collections import Counter

def CheckPitagoras(a,b,c):
    if a*a + b*b == c*c:
        return True
    else:
        return False

triplets = []

target = 1000

for a in range(1,int(target/3)):
    for b in range(a + 1, a + int((target - a)/2) + 1):
        for c in range(b + 1, target - a - b + 1):
            if CheckPitagoras(a,b,c):
                triplets.append([a,b,c])

sums = []

for i in triplets:
    answer = 0
    for j in i:
        answer = answer + j
    sums.append(answer)

print(Counter(sums))