import random
import time
import multiprocessing

start = time.time()

arr = []

# Заполнение массива числами от 1 до 1000000
for _ in range(1000001):
    arr.append(random.randrange(1, 100))


def calculate_sums(start, end, array):
    partial_sum = 0
    for i in range(start, end):
        partial_sum += arr[i]
    array.append(partial_sum)


if __name__ == "__main__":
    ranges = [
        (0, 250000),
        (250000, 500000),
        (500000, 750000),
        (750000, 1000000)
    ]

    # Общий список для хранения частичных сумм
    with multiprocessing.Manager() as manager:
        partial_sums = manager.list()

        processes = []
        for r in ranges:
            p = multiprocessing.Process(target=calculate_sums, args=(r[0], r[1], partial_sums))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        total_sum = sum(partial_sums)
        print(f"Сумма элементов массива: {total_sum}")
        print(f'Время работы: {round(time.time() - start, 2)}')