# Project Euler Problem 67
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

f = open("p067_triangle.txt", "r")
content = f.read()
str_list = content.splitlines()
f.close()

full_list = []

for i in str_list:
    a = [int(j) for j in i.split()]
    full_list.append(a)

full_list.reverse()

for i in range(len(full_list)-1):
    a = full_list.pop(0)
    for j in range(len(full_list[0])):
        full_list[0][j] = max(full_list[0][j]+a[j],full_list[0][j]+a[j+1])

print(full_list)