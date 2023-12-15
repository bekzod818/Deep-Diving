lst = [1, 2, 3, 4, 5, 6, 7]

iter1 = iter(lst)

print(iter1)

print(next(iter1))  # 1
print(next(iter1))  # 2
print(next(iter1))  # 3
print(next(iter1))  # 4
print(next(iter1))  # 5
print(next(iter1))  # 6
print(next(iter1))  # 7
# print(next(iter1)) # StopIteration error


# Bunda biz generatordan foydalanganda avtomatik iter() funksiyasiga asoslangan object yaratadi
numbers = (i for i in range(1, 1000))

for item in numbers:
    print(item)
