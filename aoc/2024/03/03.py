with open("input (1).txt", "r") as f:
#with open("sample.txt", "r") as f:
    lines = (line.strip() for line in f.readlines())

# 1
l, r = [], []
for line in lines:
    line = line.split()
    l.append(int(line[0]))
    r.append(int(line[-1]))

l.sort()
r.sort()
res1 = sum(abs(lnum - rnum) for (lnum, rnum) in zip(l, r))
print(res1)

# 2
from collections import Counter
rcounter = Counter(r)
res2 = sum(lnum * rcounter[lnum] for lnum in l)
print(res2)