from itertools import combinations

# Input
input_file = "input"
with open(f"{input_file}.txt", "r") as f:
    edges = [line.strip().split("-") for line in f.readlines()]

# Adjacency list
adj = {}
for u, v in edges:
    if u not in adj:
        adj[u] = set()
    if v not in adj:
        adj[v] = set()
    adj[u].add(v)
    adj[v].add(u)

# 1
tnodes = {v for v in adj if v.startswith("t")}
t3cliques = set()
for tnode in tnodes:
    for u, v in combinations(adj[tnode], 2):
        if u in adj[v]:
            t3cliques.add(frozenset([tnode, u, v]))
res1 = len(t3cliques)
print(res1)

# 2
import networkx as nx

G = nx.Graph()
G.add_edges_from(edges)
max_clique = max(nx.find_cliques(G), key=len)
res2 = ",".join(sorted(max_clique))
print(res2)