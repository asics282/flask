import random, time

start = time.time()

arr = []

# заполнение массива числами от 1 до 1000000
for _ in range(1000000):
    arr.append(random.randrange(1, 100))

summa = 0
for i in arr:
    summa += i

print(summa)
print(f'Время работы: {round(time.time() - start, 2)}')