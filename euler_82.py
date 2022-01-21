# Project Euler Problem 82
# NOTE: This problem is a more challenging version of Problem 81.

# The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

 
# Find the minimal path sum from the left column to the right column in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

import time
import math


start = time.time()

f = open("p082_matrix.txt", "r")
content = f.read()
str_list = content.splitlines()
f.close()

full_list = []

answer = 0

for i in str_list:
    a = [int(j) for j in i.split(',')]
    full_list.append(a)

new_list = []

for i in range(len(full_list)):
    new_list.append([full_list[i][-1]])

for i in range(2, 3):
    b = full_list[0][-i] + full_list[0][-(i - 1)]
    c = 
    for j in range(len(full_list)):
        new_list[j] = [full_list[j][-i]] + new_list[j]

print(new_list)

end = time.time()
print("Minimum sum of matrix:", full_list[0][0])
print("Time taken:", end - start)
