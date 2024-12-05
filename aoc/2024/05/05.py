from collections import defaultdict

with open("input.txt", "r") as f:
    lines = (line.strip() for line in f.readlines())

page_successors = defaultdict(set)
for line in lines:
    if line == "":
        break
    curr, prev = line.split("|")
    page_successors[int(curr)].add(int(prev))

updates = []
for line in lines:
    updates.append([int(num) for num in line.split(",")])

# 1
def is_ordered(update):
    curr_update = set()
    for num in update:
        if page_successors[num] & curr_update:
            return False
        curr_update.add(num)
    return True

res1 = sum(update[len(update) // 2] for update in updates if is_ordered(update))
print(res1)

# 2
def order(update):
    new_update = []
    for num in update:
        new_update.append(num)
        i = len(new_update) - 2
        while i >= 0 and not is_ordered(new_update):
            new_update[i], new_update[i + 1] = new_update[i + 1], new_update[i]
            i -= 1
    return new_update

res2 = sum(order(update)[len(update) // 2] for update in updates if not is_ordered(update))
print(res2)