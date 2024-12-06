from copy import deepcopy

with open("input.txt", "r") as f:
    m = [line.strip() for line in f.readlines()]

#1
R, C = len(m), len(m[0])

guard_dir = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

rotations = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
}

def rotate(dir):
    return rotations[dir]

def get_start_position():
    for r in range(R):
        for c in range(C):
            if m[r][c] in guard_dir:
                return r, c, guard_dir[m[r][c]]
r_start, c_start, dir_start = get_start_position()

# Walk
def walk():
    r, c, dir = r_start, c_start, dir_start
    positions = set()
    while True:
        positions.add((r, c))
        dr, dc = dir
        if not (0 <= r + dr < R and 0 <= c + dc < C):
            break
        if m[r + dr][c + dc] == "#":
            dir = rotate(dir)
            continue
        r, c = r + dr, c + dc
    return len(positions)

res1 = walk()
print(res1)

# 2
def is_infinite(r_blocked, c_blocked):
    print(f"Calling is_infinite{r_blocked, c_blocked}")
    r, c, dir = r_start, c_start, dir_start
    positions = set()
    while True:
        if (r, c, dir) in positions:
            return 1
        positions.add((r, c, dir))
        dr, dc = dir
        if not (0 <= r + dr < R and 0 <= c + dc < C):
            return 0
        if m[r + dr][c + dc] == "#" or (r + dr == r_blocked and c + dc == c_blocked):
            dir = rotate(dir)
            continue
        r, c = r + dr, c + dc

res2 = sum(is_infinite(r_blocked, c_blocked) for r_blocked in range(R) for c_blocked in range(C) if m[r_blocked][c_blocked] not in "^<>v#")
print(res2)    