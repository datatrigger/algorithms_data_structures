with open("input.txt", "r") as f:
    lines = (line.strip() for line in f.readlines())
input = "".join(lines)
#input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

# 1
import re
def s1(input):
    matches = re.findall("mul\((\d+),(\d+)\)", input)
    return sum(int(match[0]) * int(match[1]) for match in matches)
print(s1(input))

# 2
do_str = ""
do = True
for i in range(len(input)):
    if input[i:i + len("do()")] == "do()":
        do = True
    if input[i:i + len("don't()")] == "don't()":
        do = False
    if do:
        do_str += input[i]
print(s1(do_str))
