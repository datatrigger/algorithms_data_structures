from collections import deque

# Input
input_file = "input"
with open(f"{input_file}.txt", "r") as f:
    lines = (line.strip() for line in f.readlines())

# 1
## Preprocess
vals = {}
for line in lines:
    if line == "":
        break
    wire, val = line.split(": ")
    vals[wire] = int(val)

gates = {}
for line in lines:
    computation, output = line.split(" -> ")
    gates[output] = computation.split(" ")

def compute(output):
    input1, operation, input2 = gates[output]
    if operation == "AND":
        return vals[input1] & vals[input2]
    elif operation == "OR":
        return vals[input1] | vals[input2]
    elif operation == "XOR":
        return vals[input1] ^ vals[input2]
    else:
        raise ValueError("Unknown operation")

## Topsort the gates
graph = {}
for dst in gates:
    src1, _, src2 = gates[dst]
    if src1 not in graph:
        graph[src1] = []
    if src2 not in graph:
        graph[src2] = []
    if dst not in graph:
        graph[dst] = []
    graph[src1].append(dst)
    graph[src2].append(dst)

in_degree = {v: 0 for v in graph}
for v in graph:
    for nei in graph[v]:
        in_degree[nei] += 1

queue = deque([v for v in in_degree if in_degree[v] == 0])
topsort = []
while queue:
    v = queue.popleft()
    if v not in vals:
        topsort.append(v)
    for nei in graph[v]:
        in_degree[nei] -= 1
        if in_degree[nei] == 0:
            queue.append(nei)

## Compute
for output in topsort:
    vals[output] = compute(output)
zwires = sorted([output for output in vals.keys() if output.startswith("z")])
num = 0
for i, zwire in enumerate(zwires):
    num |= vals[zwire] << i
print(num)

# 2
# I could not figure out a programmatic approach for this one.
# Get all edges + node type (x, y, z, and gate, or gate, xor gate)
# Represent graph and visually identify swapped wires.

subgraph = {subgraph: set() for subgraph in ("x", "y", "z", "AND", "OR", "XOR")}
edges = []
for o, (i1, op, i2) in gates.items():
    subgraph[op].add(o) # Gate type
    edges.append([i1, o]) # Edge 1
    edges.append([i2, o]) # Edge 1
    for node in [i1, i2, o]: # x, y, z nodes
        first_letter = node[0]
        if first_letter in "xyz":
            subgraph[first_letter].add(node)

for type, s in subgraph.items():
    subgraph[type] = sorted(s)

from graphviz import Digraph
# https://graphviz.org/doc/info/colors.html
color = {
    "x": "lightgrey",
    "y": "darkgrey",
    "z": "red",
    "AND": "blue",
    "OR": "green",
    "XOR": "yellow",
}
graph = Digraph('G')
for type in ("x", "y", "z"):
    with graph.subgraph(name=type) as s:
        s.attr("node", color=color[type], style="filled")
        s.edges(
            [(subgraph[type][i], subgraph[type][i + 1]) for i in range(len(subgraph[type]) - 1)]
        )
for type in ("AND", "OR", "XOR"):
    with graph.subgraph(name=type) as s:
        s.attr("node", color=color[type], style="filled")
        for node in subgraph[type]:
            s.node(node)
graph.edges(edges)
graph.save("circuit.dot")
#https://dreampuf.github.io/GraphvizOnline/?engine=dot