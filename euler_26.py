# Project Euler Problem 26
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


def CycleLength(d,s):
    div_l = []
    rem_l = []
    dig_l = []
    r = 0
    while (d not in div_l) or (r not in rem_l):
        dig_l.append(int(d/s))
        div_l.append(d)
        r = d % s
        rem_l.append(r)
        d = r * 10
    a = len(dig_l)
    return a

answer = 0
cur_max = 0

for i in range(1,1000):
    a = CycleLength(1,i)
    if a > cur_max:
        cur_max = a
        answer = i

print(answer)