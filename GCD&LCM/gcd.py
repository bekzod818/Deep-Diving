def gcd(a, b):
    if a < b:
        return gcd(a, b - a)
    elif a > b:
        return gcd(a - b, b)
    else:
        return a


print(gcd(68, 119))


# Euclid's Algorithm
def compute_gcd(a, b):
    if b == 0:
        return a
    else:
        return compute_gcd(b, a % b)


print(compute_gcd(68, 119))
