# Project Euler Problem 76
# It is possible to write five as a sum in exactly six different ways:

# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1

# How many different ways can one hundred be written as a sum of at least two positive integers?

import time

start = time.time()

target = 100

ways_to_sum = [0] * (target + 1)

ways_to_sum[0] = 1

for i in range(1, target):
    for j in range(i, target + 1):
        ways_to_sum[j] += ways_to_sum[j - i]

end = time.time()
print("Ways to sum to", target, ":", ways_to_sum[target])
print("Time taken:", end - start)
