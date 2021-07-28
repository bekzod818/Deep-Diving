def fib(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

num = int(input("n = "))
for i in range(1, num + 1):
    print(fib(i), end=" ")