from collections import defaultdict, deque
from functools import reduce
from time import sleep

input_file = "input"
with open(f"{input_file}.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

#1
X, Y = 101, 103
if input_file == "sample":
    X, Y = 11, 7

p, v = [], []
for line in lines:
    position, velocity = line.split()
    px, py = position[2:].split(",")
    vx, vy = velocity[2:].split(",")
    px, py = int(px), int(py)
    vx, vy = int(vx), int(vy)
    p.append([px, py])
    v.append([vx, vy])

def get_position(px, py, vx, vy, time):
    return (px + (vx * time)) % (X), (py + (vy * time)) % (Y)

def get_quadrant(px, py):
    midx, midy = X // 2, Y // 2
    if px == midx or py == midy:
        return (-1, -1)
    return (px // (midx + 1), py // (midy + 1))

n = len(p)
def get_quadrant_counts(time):
    quadrant_count = defaultdict(int)
    for i in range(n):
        px, py = p[i]
        vx, vy = v[i]
        ptime = get_position(px, py, vx, vy, time)
        quadrant = get_quadrant(*ptime)
        if quadrant == (-1, -1):
            continue
        quadrant_count[quadrant] += 1
    return quadrant_count

print(reduce(lambda x, y: x * y, get_quadrant_counts(100).values()))

# 2
def get_positions_at_time(time):
    new_positions = []
    for i in range(n):
        px, py = p[i]
        vx, vy = v[i]
        new_positions.append(get_position(px, py, vx, vy, time))
    return new_positions

def count_components(m):
    R, C = len(m), len(m[0])
    def dfs(r, c):
        if min(r, c) < 0 or r >= R or c >= C or m[r][c] == "." or (r, c) in visited:
            return
        visited.add((r, c))
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            dfs(r + dr, c + dc)
        return
    visited = set()
    components = 0
    for r in range(R):
        for c in range(C):
            if (r, c) not in visited and m[r][c] == "*":
                dfs(r, c)
                components += 1
    return components

def prettyprint(positions, threshold=float("inf")):
    m = [["."] * X for _ in range(Y)]
    for px, py in positions:
        m[py][px] = "*"
    components = count_components(m)
    if components < threshold:
        for r in range(len(m)):
            print("".join(m[r]))
        print(time, components)
    return

# Get cycle length: 10403
# time = 0
# while True:
#     time += 1
#     positions = get_positions_at_time(time)
#     if all([p1x == p2x and p1y == p2y for ((p1x, p1y), (p2x, p2y)) in zip(p, positions)]):
#         print(time)
#         break

time = 0
threshold = 200
while time < 10403:
    time += 1
    positions = get_positions_at_time(time)
    prettyprint(positions, threshold)