with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

R, C = len(lines), len(lines[0])
m = [[0] * C for _ in range(R)]
for r in range(R):
    for c in range(C):
        m[r][c] = int(lines[r][c])

#1
def dfs(r, c, prev, visited):
    valid = (
        0 <= r < R
        and 0 <= c < C
        and (r, c) not in visited
        and m[r][c] == prev + 1
    )
    if not valid:
        return 0
    
    visited.add((r, c))
    if m[r][c] == 9:
        return 1
    deltas = ((0, 1), (0, -1), (-1, 0), (1, 0))
    count = 0
    for dr, dc in deltas:
        count += dfs(r + dr, c + dc, prev + 1, visited)
    return count

res1 = sum(dfs(r, c, -1, set()) for r in range(R) for c in range(C) if m[r][c] == 0)
print(res1)

#2
# A set is not needed:
# infinite loops are not possible
# as paths must be increasing
def dfs2(r, c, prev):
    valid = (
        0 <= r < R
        and 0 <= c < C
        and m[r][c] == prev + 1
    )
    if not valid:
        return 0
    if m[r][c] == 9:
        return 1
    deltas = ((0, 1), (0, -1), (-1, 0), (1, 0))
    count = 0
    for dr, dc in deltas:
        count += dfs2(r + dr, c + dc, prev + 1)
    return count

res2 = sum(dfs2(r, c, -1) for r in range(R) for c in range(C) if m[r][c] == 0)
print(res2)