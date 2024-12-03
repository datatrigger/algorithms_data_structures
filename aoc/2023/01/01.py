with open("input.txt", "r") as f:
#with open("sample.txt", "r") as f:
    lines = (line.strip() for line in f.readlines())

# 1
def get_number(line):
    first = last = "0"
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

