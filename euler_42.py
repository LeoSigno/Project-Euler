# Project Euler Problem 42
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

def WordSum(n):
    a = 0
    for c in n:
        b = ord(c.lower()) - ord('a') + 1
        a = a + b
    return a

def GenTriangleNumbers(n):
    l = []
    for i in range(1, n + 1):
        l.append(int(0.5 * i * (i + 1)))
    return l

f = open("p042_words.txt", "r")
a = f.read().replace("\"","")

b = [i for i in a.split(',')]

values = []

for i in b:
    values.append(WordSum(i))

tri = GenTriangleNumbers(20)

c = 0

for i in values:
    if i in tri:
        c = c + 1

print("Total number of triangle words: ",c)