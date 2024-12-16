import heapq

input_file = "sample"
with open(f"{input_file}.txt", "r") as f:
    m = [line.strip() for line in f.readlines()]

directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

#1

R, C = len(m), len(m[0])
for r in range(R):
    for c in range(C):
        if m[r][c] == "S":
            start = (r, c, 0, 1)
            rstart, cstart = r, c
        if m[r][c] == "E":
            rend, cend = r, c

def get_shortest_path_distance():
    heap = [(0, start)]
    visited = set()
    while heap:
        d, (r, c, curr_dr, curr_dc) = heapq.heappop(heap)
        if (r, c, curr_dr, curr_dc) in visited:
            continue
        visited.add((r, c, curr_dr, curr_dc))
        if r == rend and c == cend:
            return d
        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            if m[r + dr][c + dc] == "#":
                continue
            if dr == curr_dr and dc == curr_dc:
                heapq.heappush(heap, (d + 1, (r + dr, c + dc, dr, dc)))
            else:
                heapq.heappush(heap, (d + 1000, (r, c, dr, dc)))
    return v
shortest_distance = get_shortest_path_distance()
print(shortest_distance)

#2
parents = {}
heap = [(0, start, start)] #cost, node, parent
tiles = set([(rstart, cstart), (rend, cend)])
while heap:
    d, (r, c, curr_dr, curr_dc), parent = heapq.heappop(heap)
    if (r, c, curr_dr, curr_dc) in parents:
        continue
    parents[(r, c, curr_dr, curr_dc)] = parent
    if r == rend and c == cend and d == shortest_distance:
        print(f"Found {r, c, curr_dr, curr_dc}")
        pr, pc, pdr, pdc = parent
        while not(pr == rstart and pc == cstart and pdr == 0 and pdc == 1):
            tiles.add((pr, pc))
            pr, pc, pdr, pdc = parents[(pr, pc, pdr, pdc)]
    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        if m[r + dr][c + dc] == "#":
            continue
        if dr == curr_dr and dc == curr_dc:
            heapq.heappush(heap, (d + 1, (r + dr, c + dc, dr, dc), (r, c, curr_dr, curr_dc)))
        else:
            heapq.heappush(heap, (d + 1000, (r, c, dr, dc), (r, c, curr_dr, curr_dc)))

print(len(tiles))
