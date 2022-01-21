# Euler Project Problem 6
# The sum of the squares of the first ten natural numbers is 385
# The square of the sum of the first ten natural numbers is 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math

a = 0

for i in range(1,101,1):
    a = a + i*i

print("Sum of Squares: ",a)

b = 0

for i in range(1,101,1):
    b = b + i

b = b*b

print("Square of Sums: ",b)

c = b - a

print("Difference: ",c)