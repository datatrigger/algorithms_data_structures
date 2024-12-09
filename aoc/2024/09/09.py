with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
line = lines[0]

#1
s = []
for i, count in enumerate(line):
    if is_free := i % 2:
        s += [-1] * int(count)
    else:
        s += [i // 2] * int(count)

l, r = 0, len(s) - 1
while l < r:
    if s[l] != -1:
        l += 1
    elif s[r] == -1:
        r -= 1
    else:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

res1 = 0
for i, id in enumerate(s):
    if id == -1:
        break
    res1 += i * id
print(res1)

#2
s = []
indices, counts = {}, {}
for i, count in enumerate(line):
    if is_free := i % 2:
        s += [-1] * int(count)
    else:
        id = i // 2
        indices[id] = len(s)
        counts[id] = int(count)
        s += [id] * int(count)

for id in sorted(indices.keys(), reverse=True):
    print(id)
    id_index, id_count = indices[id], counts[id]
    for i in range(id_index):        
        if i + id_count - 1 < len(s) and all([s[j] == -1 for j in range(i, i + id_count)]):
            s[id_index:id_index + id_count] = [-1] * id_count
            s[i:i + id_count] = [id] * id_count
            break

res2 = sum(i * id for (i, id) in enumerate(s) if id != -1)
print(res2)