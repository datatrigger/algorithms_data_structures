from math import floor, log10
import itertools

with open("input.txt", "r") as f:
    stones = [line.strip() for line in f.readlines()][0].split()
stones = [int(stone) for stone in stones]

#1
def change(stone):
    if int(stone) == 0:
        return [1]
    ndigits = floor(log10(stone)) + 1
    if (floor(log10(stone)) + 1) % 2 == 0:
        half = ndigits // 2
        return [stone // (10 ** half), stone % (10 ** half)]
    return [2024 * stone]

new_stones = stones
for i in range(25):
    new_stones = itertools.chain.from_iterable(map(change, new_stones))
res1 = sum(1 for _ in new_stones)
print(res1)

#2
cache = {}
def f(stone, n):
    if n == 0:
        return 1
    if (stone, n) not in cache:
        cache[(stone, n)] = sum(f(stone, n - 1) for stone in change(stone))
    return cache[(stone, n)]        

res2 = sum(f(stone, 75) for stone in stones)
print(res2)