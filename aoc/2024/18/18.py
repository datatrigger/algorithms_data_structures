from collections import deque
DELTAS = ((0, 1), (0, -1), (1, 0), (-1, 0))

# Input
input_file = "input"
with open(f"{input_file}.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# 1
n_grid, n_blocks = 70, 1024
blocks = set()
for line in lines[:n_blocks]:
    y, x = line.split(",")
    blocks.add((int(x), int(y)))

def bfs():
    visited = set([(0, 0)])
    queue = deque([(0, 0)])
    length = -1
    while queue:
        length += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            if r == n_grid and c == n_grid:
                return length
            for dr, dc in DELTAS:
                valid = (
                    0 <= r + dr <= n_grid
                    and 0 <= c + dc <= n_grid
                    and (r + dr, c + dc) not in blocks
                    and (r + dr, c + dc) not in visited
                )
                if valid:
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
    return -1

print(bfs())

# 2
# Execution is reasonable but a few seconds
# This could be enhanced with binary search
blocks = set()
for line in lines:
    y, x = line.split(",")
    blocks.add((int(x), int(y)))
    if bfs() == -1:
        break
print(y, x)
