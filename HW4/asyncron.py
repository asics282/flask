import asyncio
import random
import time

arr = [random.randint(1, 100) for _ in range(1000000)]

async def calculate_sums(start, end):
    partial_sum = 0
    for i in range(start, end):
        partial_sum += arr[i]
    partial_sums.append(partial_sum)

partial_sums = []

async def main():
    start_time = time.time()

    ranges = [
        (0, 250000),
        (250000, 500000),
        (500000, 750000),
        (750000, 1000000)
    ]

    tasks = []
    for r in ranges:
        task = asyncio.create_task(calculate_sums(*r))
        tasks.append(task)

    await asyncio.gather(*tasks)

    total_sum = sum(partial_sums)

    print(f"Сумма элементов массива: {total_sum}")
    print(f'Время выполнения (асинхронность): {round(time.time() - start_time, 2)} сек')

if __name__ == "__main__":
    asyncio.run(main())
