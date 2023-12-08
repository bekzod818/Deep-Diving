from math import isqrt


def printnum(func):
    def wrapper(nums):
        prime = func(nums)
        return " ".join(str(i) for i in prime)

    return wrapper


@printnum
def primes_less_than(n):
    if n <= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, isqrt(n) + 1):
        if is_prime[i]:
            for x in range(i * i, n, i):
                is_prime[x] = False

    return [i for i in range(n) if is_prime[i]]


n = int(input())
print(primes_less_than(n))
