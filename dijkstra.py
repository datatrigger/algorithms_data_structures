#!/usr/bin/python3

# Input graph
edges = [
    ("A", "B", 2),
    ("A", "D", 8),
    ("B", "D", 5),
    ("B", "E", 6),
    ("D", "E", 3),
    ("D", "F", 2),
    ("E", "F", 1),
    ("E", "C", 9),
    ("F", "C", 3)
]
reversed_edges = [(dst, src, distance) for (src, dst, distance) in edges]
edges.extend(reversed_edges)

# Shortest paths from node A:
# {"A": 0, "B": 2, "C": 12, "D": 7, "E": 8, "F": 9}

# Build adjacency list
adj = {}
for src, dst, distance in edges:
    if src not in adj:
        adj[src] = []
    if dst not in adj:
        adj[dst] = []
    adj[src].append((dst, distance))

# Compute shortest paths
import heapq
def shortest_paths(adj: dict[str: tuple[str, int]], start_node: str) -> dict[str: int]:
    res, heap = {}, [(0, start_node)]
    while heap:
        distance, vertice = heapq.heappop(heap)
        if vertice in res:
            continue
        res[vertice] = distance
        for v_neighbor, v_distance in adj[vertice]:
            heapq.heappush(heap, (distance + v_distance, v_neighbor))
    return res

print(shortest_paths(adj, "A"))