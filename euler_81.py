# Project Euler Problem 81
# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

 
# Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

import time
import math


start = time.time()

f = open("p081_matrix.txt", "r")
content = f.read()
str_list = content.splitlines()
f.close()

full_list = []

answer = 0

for i in str_list:
    a = [int(j) for j in i.split(',')]
    full_list.append(a)

for i in range(2, len(full_list) + 1):
    full_list[-i][-1] += full_list[-(i - 1)][-1]
    
for i in range(2, len(full_list[-1]) + 1):
    full_list[-1][-i] += full_list[-1][-(i - 1)]

for i in range(2, len(full_list) + 1):
    for j in range(2, len(full_list[-i]) + 1):
        a = full_list[-i][-j] + full_list[-(i - 1)][-j]
        b = full_list[-i][-j] + full_list[-i][-(j - 1)]
        full_list[-i][-j] = min(a, b)

end = time.time()
print("Minimum sum of matrix:", full_list[0][0])
print("Time taken:", end - start)
