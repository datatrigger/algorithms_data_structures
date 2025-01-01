def pprint(m):
    for r in range(len(m)):
        print(m[r])

# Input
input_file = "input"
with open(f"{input_file}.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

keys_and_locks = []
curr = []
for line in lines:
    if line == "":
        keys_and_locks.append(curr.copy())
        curr = []
        continue
    curr.append(line)
else:
    keys_and_locks.append(curr.copy())

locks, keys = [], []
for thing in keys_and_locks:
    if thing[0] == "#####":
        locks.append(thing[1:])
    else:
        keys.append(thing[:-1])

R, C = 6, 5
def heights(thing):
    h = []
    for c in range(C):
        h.append(sum(thing[r][c] == "#" for r in range(R)))
    return h

def fit(lock, key):
    for l, k in zip(heights(lock), heights(key)):
        if l + k >= R:
            return 0
    return 1

res1 = sum(fit(lock, key) for key in keys for lock in locks)
print(res1)

# 2
# No part 2 on day 25!