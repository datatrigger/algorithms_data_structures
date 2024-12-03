with open("input.txt", "r") as f:
#with open("sample.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# 1
def get_number(line):
    for c in line:
        if c.isdigit():
            first = c
            break
    for c in reversed(line):
        if c.isdigit():
            last = c
            break
    return int(first + last)

res1 = sum(get_number(line) for line in lines)
print(res1)

# 2
nums = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def get_number2(line):
    first = last = ""
    i = 0
    while i < len(line) and not first:
        if line[i].isdigit():
            first = line[i]
        for key, val in nums.items():
            if line[i:i + len(key)] == key:
                first = val
        i += 1
    i = len(line) - 1
    while i >= 0 and not last:
        if line[i].isdigit():
            last = line[i]
        for key, val in nums.items():
            if line[i:i + len(key)] == key:
                last = val
        i -= 1
    return int(first + last)

res2 = sum(get_number2(line) for line in lines)
print(res2)