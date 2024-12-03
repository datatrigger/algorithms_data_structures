with open("input.txt", "r") as f:
    lines = (line.strip() for line in f.readlines())
input = "".join(lines)
#input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

# 1
import re
def mul(match):
    nums = match[4:-1].split(",")
    return int(nums[0]) * int(nums[1])

matches = re.findall("mul\(\d+,\d+\)", input)
res1 = sum(mul(match) for match in matches)
print(res1)

# 2
#input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
do_str = ""
do = True
for i in range(len(input)):
    if input[i:i + len("do()")] == "do()":
        do = True
    if input[i:i + len("don't()")] == "don't()":
        do = False
    if do:
        do_str += input[i]

matches = re.findall("mul\(\d+,\d+\)", do_str)
res2 = sum(mul(match) for match in matches)
print(res2)
