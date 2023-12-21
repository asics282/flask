import random, time
import threading

start = time.time()

arr = []

# заполнение массива числами от 1 до 1000000
for _ in range(1000001):
    arr.append(random.randrange(1, 100))


def calculate_sums(start, end):
    partial_sum = 0
    for i in range(start, end):
        partial_sum += arr[i]
    partial_sums.append(partial_sum)

if __name__ == "__main__":

    ranges = [
        (0, 250000),  # Первый поток обрабатывает индексы от 0 до 249999
        (250000, 500000),  # Второй поток обрабатывает индексы от 250000 до 499999
        (500000, 750000),  # Третий поток обрабатывает индексы от 500000 до 749999
        (750000, 1000000)  # Четвертый поток обрабатывает индексы от 750000 до 999999
    ]

    # Список для хранения частичных сумм
    partial_sums = []

    threads = []
    for i in ranges:
        t = threading.Thread(target=calculate_sums, args=i)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total_sum = sum(partial_sums)
    print(f"Сумма элементов массива: {total_sum}")
    print(f'Время работы: {round(time.time() - start, 2)}')
