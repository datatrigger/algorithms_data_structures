from collections import defaultdict

with open("input.txt", "r") as f:
    m = [line.strip() for line in f.readlines()]

#1
R, C = len(m), len(m[0])
antinodes = set()
antennas = defaultdict(set)

def get_antinodes1(r, c, rnei, cnei):
    if r == rnei and c == cnei:
        return
    dr, dc = rnei - r, cnei - c
    r1, c1 = rnei + dr, cnei + dc
    r2, c2 = r - dr, c - dc
    if inbound := 0 <= r1 < R and 0 <= c1 < C:
        antinodes.add((r1, c1))
    if inbound := 0 <= r2 < R and 0 <= c2 < C:
        antinodes.add((r2, c2))
    return

for r in range(R):
    for c in range(C):
        freq = m[r][c]
        if freq.isalnum():
            antennas[freq].add((r, c))
            for rnei, cnei in antennas[freq]:
                get_antinodes1(r, c, rnei, cnei)
print(len(antinodes))

# 2
R, C = len(m), len(m[0])
antinodes = set()
antennas = defaultdict(set)

def get_antinodes2(r, c, rnei, cnei):
    if r == rnei and c == cnei:
        return
    dr, dc = rnei - r, cnei - c
    i = 0
    while inbound := 0 <= r + i * dr < R and 0 <= c + i * dc < C:
        antinodes.add((r + i * dr, c + i * dc))
        i += 1
    i = -1
    while inbound := 0 <= r + i * dr < R and 0 <= c + i * dc < C:
        antinodes.add((r + i * dr, c + i * dc))
        i -= 1
    return

for r in range(R):
    for c in range(C):
        freq = m[r][c]
        if freq.isalnum():
            antennas[freq].add((r, c))
            for rnei, cnei in antennas[freq]:
                get_antinodes2(r, c, rnei, cnei)
print(len(antinodes))