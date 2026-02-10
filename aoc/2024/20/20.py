# Note: there seems to be a unique path with no branch
# Taking this into account could simplify the approach below

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

# 1
fastest = dist_from_start[end]
cheats = set()
save = 100
for r in range(R):
    for c in range(C):
        if m[r][c] == "#":
            continue
        start_to_activation = dist_from_start[(r, c)]
        for dr, dc in DELTAS:
            deactivation_to_end = dist_from_end.get((r + 2 * dr, c + 2 * dc), float("inf"))
            cheat_time = start_to_activation + 2 + deactivation_to_end
            if cheat_time <= fastest - save:
                cheats.add((r, c, r + 2 * dr, c + 2 * dc))

print(len(cheats))

# 2
cheats = set()
save = 100
for r in range(R):
    for c in range(C):
        if m[r][c] == "#":
            continue
        start_to_activation = dist_from_start[(r, c)]
        for dr in range(-20, 21):
            for dc in range(-20, 21):
                if abs(dr) + abs(dc) > 20:
                    continue
                deactivation_to_end = dist_from_end.get((r + dr, c + dc), float("inf"))
                cheat_time = start_to_activation + abs(dr) + abs(dc) + deactivation_to_end
                if cheat_time <= fastest - save:
                    cheats.add((r, c, r + dr, c + dc))
print(len(cheats))