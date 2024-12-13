from collections import deque

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# 1
m = [list(line) for line in lines]
R, C = len(m), len(m[0])
deltas = ((0, 1), (0, -1), (-1, 0), (1, 0))

def bfs(r, c, visited):
    visited.add((r, c))
    queue = deque([(r, c)])
    area = perimeter = 0
    plant = m[r][c]
    while queue:
        r, c = queue.popleft()
        area += 1
        for dr, dc in deltas:
            if not 0 <= r + dr < R or not 0 <= c + dc < C or m[r + dr][c + dc] != plant:
                perimeter += 1
            else:
                if (r + dr, c + dc) in visited:
                    continue
                queue.append((r + dr, c + dc))
                visited.add((r + dr, c + dc))
    return area * perimeter

visited = set()
total = 0
for r in range(R):
    for c in range(C):
        if (r, c) not in visited:
            total += bfs(r, c, visited)
print(total)

# 2
# Horrible solution
# TODO: count corners instead of fences

m = [list(line) for line in lines]
R, C = len(m), len(m[0])
deltas = ((0, 1), (0, -1), (-1, 0), (1, 0))

def bfs(r, c, visited):
    visited.add((r, c))
    queue = deque([(r, c)])
    area = 0
    fences = set()
    plant = m[r][c]
    while queue:
        r, c = queue.popleft()
        area += 1
        for dr, dc in deltas:
            if not 0 <= r + dr < R or not 0 <= c + dc < C or m[r + dr][c + dc] != plant:
                if dr == 0:
                    fences.add((r + dr, c + dc, "v", c))
                else:
                    fences.add((r + dr, c + dc, "h", r))
            else:
                if (r + dr, c + dc) in visited:
                    continue
                queue.append((r + dr, c + dc))
                visited.add((r + dr, c + dc))
    nfences = 0
    while fences:
        nfences += 1
        r_fence, c_fence, dir, side = fences.pop()
        if dir == "h":
            i = 1
            while c_fence + i <= C and (r_fence, c_fence + i, "h", side) in fences:
                fences.remove((r_fence, c_fence + i, "h", side))
                i += 1
            i = 1
            while c_fence - i >= -1 and (r_fence, c_fence - i, "h", side) in fences:
                fences.remove((r_fence, c_fence - i, "h", side))
                i += 1
        else:
            i = 1
            while r_fence + i <= R and (r_fence + i, c_fence, "v", side) in fences:
                fences.remove((r_fence + i, c_fence, "v", side))
                i += 1
            i = 1
            while r_fence - i >= -1 and (r_fence - i, c_fence, "v", side) in fences:
                fences.remove((r_fence - i, c_fence, "v", side))
                i += 1
    return area, nfences

visited = set()
total = 0
for r in range(R):
    for c in range(C):
        if (r, c) not in visited:
            a, f = bfs(r, c, visited)
            total += a * f
print(total)
