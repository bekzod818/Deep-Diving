# Generator - bir marta iteratsiya qilinadigan va har bir elemntini next() funksiyasi yordamida aniq oladigan asosiysi xotiradan kam joy egallaydigan type bo'lib katta hajmli ma'lumotlarni saqlashda ishlatiladi!

gen1 = (i**2 for i in range(1, 100))

p = 1
for item in gen1:
    p *= item

# Sonlarni ko'paytirib hisoblaydi
print(p)

# Summa 0 bo'ladi sababi tepada generator bir marta foydalanildi
s1 = sum(gen1)
print(s1)

p1 = 1
for item in gen1:
    p1 *= item

# Ko'paytma 1 bo'ladi sababi tepada generator bir marta foydalanildi
print(p1)

# Xulosa Generatordan bir marta iteratsiya qilinadi va oxirida next() StopIteration xatolikni yuzaga keltiradi va shundan keyin boshqa bu generatordan foydalanilmaydi!


def seconds_generator():
    yield from range(1, 10)


# yield kalit so'zi yordamida biz generator elementlarini hosil qilishimiz mumkin
gen2 = seconds_generator()
print(sum(gen2))


# Examples
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


fibo_sequence = fibonacci_generator(10)

for num in fibo_sequence:
    print(num, end=" ")
