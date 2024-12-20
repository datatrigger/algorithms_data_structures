import sys
sys.setrecursionlimit(10000)
import heapq
from time import sleep

input_file = "input"
with open(f"{input_file}.txt", "r") as f:
    m = [line.strip() for line in f.readlines()]

#1
R, C = len(m), len(m[0])
for r in range(R):
    for c in range(C):
        if m[r][c] == "S":
            start = ((r, c), (0, 1))
        if m[r][c] == "E":
            rend, cend = r, c

def get_shortest_path_distance():
    heap = [(0, *start)]
    visited = set()
    while heap:
        d, pos, direction = heapq.heappop(heap)
        if (pos, direction) in visited:
            continue
        visited.add((pos, direction))

        if pos[0] == rend and pos[1] == cend:
            return d
        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            if m[pos[0] + dr][pos[1] + dc] == "#":
                continue
            if dr == direction[0] and dc == direction[1]:
                heapq.heappush(heap, (d + 1, (pos[0] + dr, pos[1] + dc), (dr, dc)))
            else:
                heapq.heappush(heap, (d + 1000, (pos[0], pos[1]), (dr, dc)))

shortest_distance = get_shortest_path_distance()
print(shortest_distance)

#2
from collections import defaultdict

heap = [(0, *start, (-1, -1), (-1, -1))]
shortest = {}
parents = defaultdict(set)
while heap:
    d, pos, direction, parent_pos, parent_direction = heapq.heappop(heap)
    if d > shortest_distance:
        break
    if (pos, direction) in shortest:
        if shortest[(pos, direction)] == d:
            parents[(pos, direction)].add((parent_pos, parent_direction))
        continue
    shortest[(pos, direction)] = d
    parents[(pos, direction)].add((parent_pos, parent_direction))
    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        if m[pos[0] + dr][pos[1] + dc] == "#":
            continue
        if dr == direction[0] and dc == direction[1]:
            heapq.heappush(heap, (
                d + 1,
                (pos[0] + dr, pos[1] + dc),
                (dr, dc),
                pos,
                direction
                )
            )
        else:
            heapq.heappush(heap, (d + 1000, (pos[0], pos[1]), (dr, dc), pos, direction))

end_nodes = [(r, c, dr, dc) for ((r, c), (dr, dc)) in shortest if shortest[((r, c), (dr, dc))] == shortest_distance and r == rend and c == cend]

rstart, cstart = start[0]
tiles = set([(rstart, cstart)])
def dfs(r, c, dr, dc):
    if r == rstart and c == cstart:
        return
    tiles.add((r, c))
    for ((pr, pc), (pdr, pdc)) in parents[((r, c), (dr, dc))]:
        dfs(pr, pc, pdr, pdc)

for end_node in end_nodes:
    dfs(*end_node)

print(len(tiles))