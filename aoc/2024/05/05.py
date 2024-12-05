from collections import defaultdict

with open("input.txt", "r") as f:
    lines = (line.strip() for line in f.readlines())

curr_predecessors = defaultdict(set)
for line in lines:
    if line == "":
        break
    curr, prev = line.split("|")
    curr_predecessors[int(curr)].add(int(prev))

updates = []
for line in lines:
    updates.append([int(num) for num in line.split(",")])

# 1
def is_ordered(update):
    curr = set()
    for num in update:
        if curr_predecessors[num] & curr:
            return False
        curr.add(num)
    return True

res1 = sum(update[len(update) // 2] for update in updates if is_ordered(update))
print(res1)

# 2
def order(update):
    update_ordered = []
    for num in update:
        update_ordered.append(num)
        i = len(update_ordered) - 2
        while i >= 0 and not is_ordered(update_ordered):
            update_ordered[i], update_ordered[i + 1] = update_ordered[i + 1], update_ordered[i]
            i -= 1
    return update_ordered

res2 = sum(order(update)[len(update) // 2] for update in updates if not is_ordered(update))
print(res2)