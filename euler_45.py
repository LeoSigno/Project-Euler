# Project Euler Problem 45
# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

# Triangle	 	    Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	 	Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
# Hexagonal	 	    Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.

# Find the next triangle number that is also pentagonal and hexagonal.

def IsPentagon(n):
    if (1 + (24 * n + 1) ** 0.5) % 6 == 0:
        return True
    return False

def IsHexagon(n):
    if (1 + (8 * n + 1) ** 0.5) % 4 == 0:
        return True
    return False

i = 286

found = False

while not found:
    n = i * (i + 1) * 0.5
    print("Testing number: ", int(n), "     ", end = "\r")
    if IsPentagon(n) and IsHexagon(n):
        print("\n\nFount it! Number is ", int(n))
        found = True
    i = i + 1