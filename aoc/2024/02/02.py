with open("input.txt", "r") as f:
    lines = sum(line.strip() for line in f.readlines()))

# 1
def is_safe(report):
    if len(report) == 0:
        return False
    
    if report[1] - report[0] > 0:
        trend = 1
        prev = report[0] - 1
    elif report[1] - report[0] < 0:
        trend = -1
        prev = report[0] + 1
    else:
        return False
    
    for num in report:
        safe =(
            trend * (num - prev) > 0
            and 1 <= abs(num - prev) <= 3
        )
        if not safe:
            return False
        prev = num
    return True

count_safe = 0
for line in lines:
    nums = list(map(int, line.split()))
    count_safe += int(is_safe(nums))

print(count_safe)

# 2
count_safe = 0
for line in lines:
    nums = list(map(int, line.split()))
    if any([is_safe(nums[:i] + nums[i + 1:]) for i in range(len(nums) + 1)]):
        count_safe += 1

print(count_safe)