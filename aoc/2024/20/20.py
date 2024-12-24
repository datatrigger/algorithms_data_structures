from collections import deque
DELTAS = ((0, 1), (0, -1), (1, 0), (-1, 0))

# Input
input_file = "input"
with open(f"{input_file}.txt", "r") as f:
    m = [list(line.strip()) for line in f.readlines()]

# Preprocessing
R, C = len(m), len(m[0])
for r in range(R):
    for c in range(C):
        if m[r][c] == "S":
            start = r, c
        if m[r][c] == "E":
            end = r, c

# Get shortest distances from S/to E for all valid nodes
def bfs(source):
    queue = deque([source])
    distances = {source: 0}
    d = 0
    while queue:
        d += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in DELTAS:
                if (
                    0 <= r + dr < R
                    and 0 <= c + dc < C
                    and not m[r + dr][c + dc] == "#"
                    and not (r + dr, c + dc) in distances
                ):
                    queue.append((r + dr, c + dc))
                    distances[(r + dr, c + dc)] = d
    return distances

dist_from_start = bfs(start)
dist_from_end = bfs(end)

# Cheat
fastest = dist_from_start[end]
cheats = 0
save = 100
for r in range(R):
    for c in range(C):  
        if not m[r][c] == "#":
            continue
        start_to_wall = 1 + min(
            dist_from_start.get((r + dr, c + dc), float("inf"))
            for (dr, dc) in DELTAS
            )
        for dr, dc in DELTAS:
            wall_to_end = 1 + dist_from_end.get((r + dr, c + dc), float("inf"))
            cheat_time = start_to_wall + wall_to_end
            if cheat_time <= fastest - save:
                cheats += 1

print(cheats)  