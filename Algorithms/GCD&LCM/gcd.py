def gcd(a, b):
    if a < b:
        return gcd(a, b - a)
    elif a > b:
        return gcd(a - b, b)
    else:
        return a

print(gcd(68, 119))

# Euclid's Algorithm
def computeGcd(a, b):
    if b == 0:
        return a
    else:
        return computeGcd(b, a%b)

print(computeGcd(68, 119))