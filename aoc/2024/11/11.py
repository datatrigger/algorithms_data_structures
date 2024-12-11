from math import floor, log10
import itertools

with open("input.txt", "r") as f:
    stones = [line.strip() for line in f.readlines()][0].split()

stones = (int(stone) for stone in stones)

def change(num):
    if int(num) == 0:
        return [1]
    ndigits = floor(log10(num)) + 1
    if (floor(log10(num)) + 1) % 2 == 0:
        half = ndigits // 2
        return [num // (10 ** half), num % (10 ** half)]
    return [2024 * num]

n = 75
for i in range(n):
    stones = itertools.chain.from_iterable(map(change, stones))
print(sum(1 for _ in stones))