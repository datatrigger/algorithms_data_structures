with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

#1
def is_valid(line, part=1):
    val, nums = line.split(":")
    val, nums = int(val), [int(num) for num in nums.strip().split(" ")]

    cache = {}
    def f(i, curr):
        if i == len(nums):
            return curr == val
        if (i, curr) not in cache:
            add = f(i + 1, curr + nums[i])
            multiply = f(i + 1, curr * nums[i])
            cache[(i, curr)] = add or multiply
            if part == 2:
                concat = f(i + 1, int(str(curr) + str(nums[i])))
                cache[(i, curr)] = cache[(i, curr)] or concat
        return cache[(i, curr)]
    return val if f(0, 0) else 0

res1 = sum(is_valid(line, part=1) for line in lines)
print(res1)

#2
res2 = sum(is_valid(line, part=2) for line in lines)
print(res2)