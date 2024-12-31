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
        s.attr(style='filled', color=color[type])
        s.edges(
            [(subgraph[type][i], subgraph[type][i + 1]) for i in range(len(subgraph[type]) - 1)]
        )
for type in ("AND", "OR", "XOR"):
    with graph.subgraph(name=type) as s:
        s.attr(style='filled', color=color[type])
        for node in subgraph[type]:
            s.node(node)
graph.edges(edges)
graph.save("circuit.dot")
#https://dreampuf.github.io/GraphvizOnline/?engine=dot#digraph%20G%20%7B%0A%09subgraph%20x%20%7B%0A%09%09color%3Dlightgrey%20style%3Dfilled%0A%09%09x00%20-%3E%20x01%0A%09%09x01%20-%3E%20x02%0A%09%09x02%20-%3E%20x03%0A%09%09x03%20-%3E%20x04%0A%09%09x04%20-%3E%20x05%0A%09%09x05%20-%3E%20x06%0A%09%09x06%20-%3E%20x07%0A%09%09x07%20-%3E%20x08%0A%09%09x08%20-%3E%20x09%0A%09%09x09%20-%3E%20x10%0A%09%09x10%20-%3E%20x11%0A%09%09x11%20-%3E%20x12%0A%09%09x12%20-%3E%20x13%0A%09%09x13%20-%3E%20x14%0A%09%09x14%20-%3E%20x15%0A%09%09x15%20-%3E%20x16%0A%09%09x16%20-%3E%20x17%0A%09%09x17%20-%3E%20x18%0A%09%09x18%20-%3E%20x19%0A%09%09x19%20-%3E%20x20%0A%09%09x20%20-%3E%20x21%0A%09%09x21%20-%3E%20x22%0A%09%09x22%20-%3E%20x23%0A%09%09x23%20-%3E%20x24%0A%09%09x24%20-%3E%20x25%0A%09%09x25%20-%3E%20x26%0A%09%09x26%20-%3E%20x27%0A%09%09x27%20-%3E%20x28%0A%09%09x28%20-%3E%20x29%0A%09%09x29%20-%3E%20x30%0A%09%09x30%20-%3E%20x31%0A%09%09x31%20-%3E%20x32%0A%09%09x32%20-%3E%20x33%0A%09%09x33%20-%3E%20x34%0A%09%09x34%20-%3E%20x35%0A%09%09x35%20-%3E%20x36%0A%09%09x36%20-%3E%20x37%0A%09%09x37%20-%3E%20x38%0A%09%09x38%20-%3E%20x39%0A%09%09x39%20-%3E%20x40%0A%09%09x40%20-%3E%20x41%0A%09%09x41%20-%3E%20x42%0A%09%09x42%20-%3E%20x43%0A%09%09x43%20-%3E%20x44%0A%09%7D%0A%09subgraph%20y%20%7B%0A%09%09color%3Ddarkgrey%20style%3Dfilled%0A%09%09y00%20-%3E%20y01%0A%09%09y01%20-%3E%20y02%0A%09%09y02%20-%3E%20y03%0A%09%09y03%20-%3E%20y04%0A%09%09y04%20-%3E%20y05%0A%09%09y05%20-%3E%20y06%0A%09%09y06%20-%3E%20y07%0A%09%09y07%20-%3E%20y08%0A%09%09y08%20-%3E%20y09%0A%09%09y09%20-%3E%20y10%0A%09%09y10%20-%3E%20y11%0A%09%09y11%20-%3E%20y12%0A%09%09y12%20-%3E%20y13%0A%09%09y13%20-%3E%20y14%0A%09%09y14%20-%3E%20y15%0A%09%09y15%20-%3E%20y16%0A%09%09y16%20-%3E%20y17%0A%09%09y17%20-%3E%20y18%0A%09%09y18%20-%3E%20y19%0A%09%09y19%20-%3E%20y20%0A%09%09y20%20-%3E%20y21%0A%09%09y21%20-%3E%20y22%0A%09%09y22%20-%3E%20y23%0A%09%09y23%20-%3E%20y24%0A%09%09y24%20-%3E%20y25%0A%09%09y25%20-%3E%20y26%0A%09%09y26%20-%3E%20y27%0A%09%09y27%20-%3E%20y28%0A%09%09y28%20-%3E%20y29%0A%09%09y29%20-%3E%20y30%0A%09%09y30%20-%3E%20y31%0A%09%09y31%20-%3E%20y32%0A%09%09y32%20-%3E%20y33%0A%09%09y33%20-%3E%20y34%0A%09%09y34%20-%3E%20y35%0A%09%09y35%20-%3E%20y36%0A%09%09y36%20-%3E%20y37%0A%09%09y37%20-%3E%20y38%0A%09%09y38%20-%3E%20y39%0A%09%09y39%20-%3E%20y40%0A%09%09y40%20-%3E%20y41%0A%09%09y41%20-%3E%20y42%0A%09%09y42%20-%3E%20y43%0A%09%09y43%20-%3E%20y44%0A%09%7D%0A%09subgraph%20z%20%7B%0A%09%09color%3Dred%20style%3Dfilled%0A%09%09z00%20-%3E%20z01%0A%09%09z01%20-%3E%20z02%0A%09%09z02%20-%3E%20z03%0A%09%09z03%20-%3E%20z04%0A%09%09z04%20-%3E%20z05%0A%09%09z05%20-%3E%20z06%0A%09%09z06%20-%3E%20z07%0A%09%09z07%20-%3E%20z08%0A%09%09z08%20-%3E%20z09%0A%09%09z09%20-%3E%20z10%0A%09%09z10%20-%3E%20z11%0A%09%09z11%20-%3E%20z12%0A%09%09z12%20-%3E%20z13%0A%09%09z13%20-%3E%20z14%0A%09%09z14%20-%3E%20z15%0A%09%09z15%20-%3E%20z16%0A%09%09z16%20-%3E%20z17%0A%09%09z17%20-%3E%20z18%0A%09%09z18%20-%3E%20z19%0A%09%09z19%20-%3E%20z20%0A%09%09z20%20-%3E%20z21%0A%09%09z21%20-%3E%20z22%0A%09%09z22%20-%3E%20z23%0A%09%09z23%20-%3E%20z24%0A%09%09z24%20-%3E%20z25%0A%09%09z25%20-%3E%20z26%0A%09%09z26%20-%3E%20z27%0A%09%09z27%20-%3E%20z28%0A%09%09z28%20-%3E%20z29%0A%09%09z29%20-%3E%20z30%0A%09%09z30%20-%3E%20z31%0A%09%09z31%20-%3E%20z32%0A%09%09z32%20-%3E%20z33%0A%09%09z33%20-%3E%20z34%0A%09%09z34%20-%3E%20z35%0A%09%09z35%20-%3E%20z36%0A%09%09z36%20-%3E%20z37%0A%09%09z37%20-%3E%20z38%0A%09%09z38%20-%3E%20z39%0A%09%09z39%20-%3E%20z40%0A%09%09z40%20-%3E%20z41%0A%09%09z41%20-%3E%20z42%0A%09%09z42%20-%3E%20z43%0A%09%09z43%20-%3E%20z44%0A%09%09z44%20-%3E%20z45%0A%09%7D%0A%09subgraph%20AND%20%7B%0A%09%09color%3Dblue%20style%3Dfilled%0A%09%09bbk%0A%09%09bjv%0A%09%09bmm%0A%09%09btc%0A%09%09btk%0A%09%09bvk%0A%09%09cpj%0A%09%09cqf%0A%09%09ctg%0A%09%09cwk%0A%09%09djc%0A%09%09djv%0A%09%09dkt%0A%09%09dnp%0A%09%09dps%0A%09%09drq%0A%09%09dsw%0A%09%09dwv%0A%09%09fcj%0A%09%09fkm%0A%09%09fmk%0A%09%09gdf%0A%09%09ggc%0A%09%09gkt%0A%09%09hfd%0A%09%09hfv%0A%09%09hhf%0A%09%09hvw%0A%09%09jbg%0A%09%09jcd%0A%09%09jmq%0A%09%09jqp%0A%09%09kfq%0A%09%09kmw%0A%09%09krw%0A%09%09ksc%0A%09%09ktf%0A%09%09kvg%0A%09%09mbg%0A%09%09mbk%0A%09%09mfg%0A%09%09mfj%0A%09%09mgr%0A%09%09mhg%0A%09%09mjp%0A%09%09mst%0A%09%09nhf%0A%09%09nhs%0A%09%09nrr%0A%09%09nrt%0A%09%09nsp%0A%09%09ntc%0A%09%09nvc%0A%09%09ptt%0A%09%09pwm%0A%09%09qdg%0A%09%09qds%0A%09%09qms%0A%09%09qqp%0A%09%09qrk%0A%09%09qvj%0A%09%09qvt%0A%09%09qwg%0A%09%09rfq%0A%09%09rgp%0A%09%09rmq%0A%09%09rns%0A%09%09rsd%0A%09%09rtp%0A%09%09rvf%0A%09%09spp%0A%09%09spv%0A%09%09sqh%0A%09%09stf%0A%09%09stn%0A%09%09tgr%0A%09%09thp%0A%09%09tnw%0A%09%09trg%0A%09%09trm%0A%09%09vgr%0A%09%09vph%0A%09%09vpn%0A%09%09vsq%0A%09%09wdw%0A%09%09wmk%0A%09%09wqh%0A%09%09z11%0A%09%09z31%0A%09%7D%0A%09subgraph%20OR%20%7B%0A%09%09color%3Dgreen%20style%3Dfilled%0A%09%09btf%0A%09%09cbc%0A%09%09cfp%0A%09%09cjs%0A%09%09cmn%0A%09%09cmt%0A%09%09ctq%0A%09%09dbd%0A%09%09dck%0A%09%09dtb%0A%09%09dtf%0A%09%09dvh%0A%09%09fgs%0A%09%09fnn%0A%09%09fpp%0A%09%09fps%0A%09%09fpv%0A%09%09gps%0A%09%09hhm%0A%09%09hjm%0A%09%09hrv%0A%09%09jcs%0A%09%09jdt%0A%09%09jgm%0A%09%09jww%0A%09%09kbg%0A%09%09nck%0A%09%09ndc%0A%09%09nhg%0A%09%09nrq%0A%09%09nwb%0A%09%09pqr%0A%09%09rfs%0A%09%09rgq%0A%09%09rmd%0A%09%09sbf%0A%09%09sqm%0A%09%09srm%0A%09%09tdr%0A%09%09tkf%0A%09%09wkt%0A%09%09wmb%0A%09%09z38%0A%09%09z45%0A%09%7D%0A%09subgraph%20XOR%20%7B%0A%09%09color%3Dyellow%20style%3Dfilled%0A%09%09bbf%0A%09%09btp%0A%09%09cbv%0A%09%09cpf%0A%09%09cpg%0A%09%09ctw%0A%09%09djk%0A%09%09dmf%0A%09%09dmh%0A%09%09dqd%0A%09%09dvq%0A%09%09dvv%0A%09%09fgk%0A%09%09fjg%0A%09%09frw%0A%09%09fvp%0A%09%09ggb%0A%09%09gjs%0A%09%09gnb%0A%09%09hfh%0A%09%09hhv%0A%09%09hnn%0A%09%09hwb%0A%09%09hwk%0A%09%09jgp%0A%09%09jws%0A%09%09kvh%0A%09%09mpb%0A%09%09ngd%0A%09%09ngk%0A%09%09pcb%0A%09%09pgj%0A%09%09rbf%0A%09%09rdf%0A%09%09rpb%0A%09%09rpv%0A%09%09rtg%0A%09%09rww%0A%09%09sbn%0A%09%09sbt%0A%09%09sjb%0A%09%09twb%0A%09%09vjq%0A%09%09vnt%0A%09%09vsd%0A%09%09wbm%0A%09%09wcd%0A%09%09z00%0A%09%09z01%0A%09%09z02%0A%09%09z03%0A%09%09z04%0A%09%09z05%0A%09%09z06%0A%09%09z07%0A%09%09z08%0A%09%09z09%0A%09%09z10%0A%09%09z12%0A%09%09z13%0A%09%09z14%0A%09%09z15%0A%09%09z16%0A%09%09z17%0A%09%09z18%0A%09%09z19%0A%09%09z20%0A%09%09z21%0A%09%09z22%0A%09%09z23%0A%09%09z24%0A%09%09z25%0A%09%09z26%0A%09%09z27%0A%09%09z28%0A%09%09z29%0A%09%09z30%0A%09%09z32%0A%09%09z33%0A%09%09z34%0A%09%09z35%0A%09%09z36%0A%09%09z37%0A%09%09z39%0A%09%09z40%0A%09%09z41%0A%09%09z42%0A%09%09z43%0A%09%09z44%0A%09%7D%0A%09rdf%20-%3E%20z21%0A%09nck%20-%3E%20z21%0A%09y12%20-%3E%20stn%0A%09x12%20-%3E%20stn%0A%09twb%20-%3E%20z41%0A%09jgm%20-%3E%20z41%0A%09cpj%20-%3E%20cmt%0A%09tgr%20-%3E%20cmt%0A%09y17%20-%3E%20jws%0A%09x17%20-%3E%20jws%0A%09cpg%20-%3E%20z14%0A%09tdr%20-%3E%20z14%0A%09x42%20-%3E%20dkt%0A%09y42%20-%3E%20dkt%0A%09jmq%20-%3E%20dck%0A%09bjv%20-%3E%20dck%0A%09wkt%20-%3E%20cwk%0A%09jgp%20-%3E%20cwk%0A%09fmk%20-%3E%20pqr%0A%09wqh%20-%3E%20pqr%0A%09jws%20-%3E%20rsd%0A%09rmd%20-%3E%20rsd%0A%09y32%20-%3E%20rns%0A%09x32%20-%3E%20rns%0A%09twb%20-%3E%20kvg%0A%09jgm%20-%3E%20kvg%0A%09nrq%20-%3E%20z09%0A%09wcd%20-%3E%20z09%0A%09btc%20-%3E%20dtb%0A%09rns%20-%3E%20dtb%0A%09ctq%20-%3E%20z20%0A%09gjs%20-%3E%20z20%0A%09dqd%20-%3E%20z18%0A%09hhm%20-%3E%20z18%0A%09hfh%20-%3E%20nhs%0A%09jdt%20-%3E%20nhs%0A%09rsd%20-%3E%20hhm%0A%09rgp%20-%3E%20hhm%0A%09x19%20-%3E%20kmw%0A%09y19%20-%3E%20kmw%0A%09dck%20-%3E%20z15%0A%09ctg%20-%3E%20z15%0A%09pqr%20-%3E%20trm%0A%09hhv%20-%3E%20trm%0A%09y08%20-%3E%20trg%0A%09x08%20-%3E%20trg%0A%09x31%20-%3E%20z31%0A%09y31%20-%3E%20z31%0A%09x14%20-%3E%20bjv%0A%09y14%20-%3E%20bjv%0A%09y26%20-%3E%20sbn%0A%09x26%20-%3E%20sbn%0A%09pgj%20-%3E%20z30%0A%09fnn%20-%3E%20z30%0A%09hwb%20-%3E%20cqf%0A%09rgq%20-%3E%20cqf%0A%09ctq%20-%3E%20fcj%0A%09gjs%20-%3E%20fcj%0A%09thp%20-%3E%20rgq%0A%09qdg%20-%3E%20rgq%0A%09y03%20-%3E%20mhg%0A%09x03%20-%3E%20mhg%0A%09sbt%20-%3E%20z05%0A%09ndc%20-%3E%20z05%0A%09nrr%20-%3E%20dvh%0A%09hfv%20-%3E%20dvh%0A%09x07%20-%3E%20djc%0A%09y07%20-%3E%20djc%0A%09dtb%20-%3E%20hvw%0A%09mpb%20-%3E%20hvw%0A%09pwm%20-%3E%20cjs%0A%09cqf%20-%3E%20cjs%0A%09dkt%20-%3E%20fpv%0A%09wdw%20-%3E%20fpv%0A%09x24%20-%3E%20djv%0A%09y24%20-%3E%20djv%0A%09vsq%20-%3E%20cfp%0A%09gkt%20-%3E%20cfp%0A%09x17%20-%3E%20rgp%0A%09y17%20-%3E%20rgp%0A%09rvf%20-%3E%20nhg%0A%09vph%20-%3E%20nhg%0A%09x44%20-%3E%20bbf%0A%09y44%20-%3E%20bbf%0A%09cjs%20-%3E%20z29%0A%09gnb%20-%3E%20z29%0A%09y30%20-%3E%20pgj%0A%09x30%20-%3E%20pgj%0A%09y27%20-%3E%20sjb%0A%09x27%20-%3E%20sjb%0A%09fpp%20-%3E%20dps%0A%09bbf%20-%3E%20dps%0A%09ggc%20-%3E%20fpp%0A%09ptt%20-%3E%20fpp%0A%09x18%20-%3E%20dqd%0A%09y18%20-%3E%20dqd%0A%09y19%20-%3E%20jgp%0A%09x19%20-%3E%20jgp%0A%09wkt%20-%3E%20z19%0A%09jgp%20-%3E%20z19%0A%09jcs%20-%3E%20z04%0A%09ngk%20-%3E%20z04%0A%09y21%20-%3E%20rdf%0A%09x21%20-%3E%20rdf%0A%09spp%20-%3E%20wkt%0A%09fkm%20-%3E%20wkt%0A%09x16%20-%3E%20vsd%0A%09y16%20-%3E%20vsd%0A%09y14%20-%3E%20cpg%0A%09x14%20-%3E%20cpg%0A%09mbk%20-%3E%20rmd%0A%09qwg%20-%3E%20rmd%0A%09y10%20-%3E%20nrr%0A%09x10%20-%3E%20nrr%0A%09x05%20-%3E%20sbt%0A%09y05%20-%3E%20sbt%0A%09y13%20-%3E%20fvp%0A%09x13%20-%3E%20fvp%0A%09gdf%20-%3E%20srm%0A%09tnw%20-%3E%20srm%0A%09x09%20-%3E%20gdf%0A%09y09%20-%3E%20gdf%0A%09nvc%20-%3E%20jdt%0A%09rpv%20-%3E%20jdt%0A%09kmw%20-%3E%20ctq%0A%09cwk%20-%3E%20ctq%0A%09vsd%20-%3E%20qwg%0A%09wmb%20-%3E%20qwg%0A%09x44%20-%3E%20mfg%0A%09y44%20-%3E%20mfg%0A%09y27%20-%3E%20qdg%0A%09x27%20-%3E%20qdg%0A%09jbg%20-%3E%20ndc%0A%09jqp%20-%3E%20ndc%0A%09x04%20-%3E%20ngk%0A%09y04%20-%3E%20ngk%0A%09hfh%20-%3E%20z12%0A%09jdt%20-%3E%20z12%0A%09ctg%20-%3E%20sqh%0A%09dck%20-%3E%20sqh%0A%09jww%20-%3E%20z23%0A%09djk%20-%3E%20z23%0A%09dtf%20-%3E%20z32%0A%09vjq%20-%3E%20z32%0A%09ngd%20-%3E%20ksc%0A%09sbf%20-%3E%20ksc%0A%09mfg%20-%3E%20z45%0A%09dps%20-%3E%20z45%0A%09x01%20-%3E%20rtg%0A%09y01%20-%3E%20rtg%0A%09tdr%20-%3E%20jmq%0A%09cpg%20-%3E%20jmq%0A%09y28%20-%3E%20pwm%0A%09x28%20-%3E%20pwm%0A%09y41%20-%3E%20hhf%0A%09x41%20-%3E%20hhf%0A%09qqp%20-%3E%20fgs%0A%09hfd%20-%3E%20fgs%0A%09wmb%20-%3E%20z16%0A%09vsd%20-%3E%20z16%0A%09pgj%20-%3E%20hfd%0A%09fnn%20-%3E%20hfd%0A%09dmf%20-%3E%20z40%0A%09nwb%20-%3E%20z40%0A%09rfs%20-%3E%20ktf%0A%09pcb%20-%3E%20ktf%0A%09y05%20-%3E%20rtp%0A%09x05%20-%3E%20rtp%0A%09vjq%20-%3E%20btc%0A%09dtf%20-%3E%20btc%0A%09fvp%20-%3E%20qrk%0A%09hjm%20-%3E%20qrk%0A%09mpb%20-%3E%20z33%0A%09dtb%20-%3E%20z33%0A%09y12%20-%3E%20hfh%0A%09x12%20-%3E%20hfh%0A%09cmt%20-%3E%20jcd%0A%09cbv%20-%3E%20jcd%0A%09tkf%20-%3E%20nrt%0A%09frw%20-%3E%20nrt%0A%09wcd%20-%3E%20tnw%0A%09nrq%20-%3E%20tnw%0A%09hwk%20-%3E%20btk%0A%09cbc%20-%3E%20btk%0A%09hhv%20-%3E%20dvq%0A%09pqr%20-%3E%20dvq%0A%09rfq%20-%3E%20nwb%0A%09bbk%20-%3E%20nwb%0A%09nhf%20-%3E%20nck%0A%09fcj%20-%3E%20nck%0A%09rww%20-%3E%20z42%0A%09kbg%20-%3E%20z42%0A%09x11%20-%3E%20hnn%0A%09y11%20-%3E%20hnn%0A%09fgs%20-%3E%20dmh%0A%09ctw%20-%3E%20dmh%0A%09y36%20-%3E%20rbf%0A%09x36%20-%3E%20rbf%0A%09y01%20-%3E%20vph%0A%09x01%20-%3E%20vph%0A%09fjg%20-%3E%20z43%0A%09fpv%20-%3E%20z43%0A%09x06%20-%3E%20pcb%0A%09y06%20-%3E%20pcb%0A%09x33%20-%3E%20spv%0A%09y33%20-%3E%20spv%0A%09y00%20-%3E%20z00%0A%09x00%20-%3E%20z00%0A%09x23%20-%3E%20djk%0A%09y23%20-%3E%20djk%0A%09x22%20-%3E%20mjp%0A%09y22%20-%3E%20mjp%0A%09wbm%20-%3E%20dwv%0A%09hrv%20-%3E%20dwv%0A%09hwb%20-%3E%20z28%0A%09rgq%20-%3E%20z28%0A%09x03%20-%3E%20wbm%0A%09y03%20-%3E%20wbm%0A%09x00%20-%3E%20drq%0A%09y00%20-%3E%20drq%0A%09x23%20-%3E%20dnp%0A%09y23%20-%3E%20dnp%0A%09wmk%20-%3E%20fnn%0A%09kfq%20-%3E%20fnn%0A%09x33%20-%3E%20mpb%0A%09y33%20-%3E%20mpb%0A%09y43%20-%3E%20fjg%0A%09x43%20-%3E%20fjg%0A%09y02%20-%3E%20btp%0A%09x02%20-%3E%20btp%0A%09hnn%20-%3E%20rpv%0A%09dvh%20-%3E%20rpv%0A%09cpf%20-%3E%20z24%0A%09btf%20-%3E%20z24%0A%09y42%20-%3E%20rww%0A%09x42%20-%3E%20rww%0A%09gps%20-%3E%20qvj%0A%09ggb%20-%3E%20qvj%0A%09sbn%20-%3E%20ntc%0A%09cmn%20-%3E%20ntc%0A%09x36%20-%3E%20gkt%0A%09y36%20-%3E%20gkt%0A%09y39%20-%3E%20vnt%0A%09x39%20-%3E%20vnt%0A%09dnp%20-%3E%20btf%0A%09nsp%20-%3E%20btf%0A%09rtp%20-%3E%20rfs%0A%09qms%20-%3E%20rfs%0A%09y29%20-%3E%20wmk%0A%09x29%20-%3E%20wmk%0A%09x24%20-%3E%20cpf%0A%09y24%20-%3E%20cpf%0A%09rtg%20-%3E%20rvf%0A%09drq%20-%3E%20rvf%0A%09sjb%20-%3E%20thp%0A%09dbd%20-%3E%20thp%0A%09bbf%20-%3E%20z44%0A%09fpp%20-%3E%20z44%0A%09x32%20-%3E%20vjq%0A%09y32%20-%3E%20vjq%0A%09vnt%20-%3E%20rfq%0A%09dvq%20-%3E%20rfq%0A%09btf%20-%3E%20stf%0A%09cpf%20-%3E%20stf%0A%09hjm%20-%3E%20z13%0A%09fvp%20-%3E%20z13%0A%09rmd%20-%3E%20z17%0A%09jws%20-%3E%20z17%0A%09rfs%20-%3E%20z06%0A%09pcb%20-%3E%20z06%0A%09fgs%20-%3E%20bmm%0A%09ctw%20-%3E%20bmm%0A%09vnt%20-%3E%20z39%0A%09dvq%20-%3E%20z39%0A%09dvv%20-%3E%20wqh%0A%09cfp%20-%3E%20wqh%0A%09mfj%20-%3E%20jgm%0A%09vgr%20-%3E%20jgm%0A%09y25%20-%3E%20qds%0A%09x25%20-%3E%20qds%0A%09qds%20-%3E%20cmn%0A%09btk%20-%3E%20cmn%0A%09kvh%20-%3E%20hfv%0A%09srm%20-%3E%20hfv%0A%09y09%20-%3E%20wcd%0A%09x09%20-%3E%20wcd%0A%09y10%20-%3E%20kvh%0A%09x10%20-%3E%20kvh%0A%09dwv%20-%3E%20jcs%0A%09mhg%20-%3E%20jcs%0A%09y16%20-%3E%20mbk%0A%09x16%20-%3E%20mbk%0A%09y43%20-%3E%20ggc%0A%09x43%20-%3E%20ggc%0A%09x34%20-%3E%20krw%0A%09y34%20-%3E%20krw%0A%09x29%20-%3E%20gnb%0A%09y29%20-%3E%20gnb%0A%09y02%20-%3E%20mgr%0A%09x02%20-%3E%20mgr%0A%09fgk%20-%3E%20mbg%0A%09sqm%20-%3E%20mbg%0A%09y40%20-%3E%20dmf%0A%09x40%20-%3E%20dmf%0A%09y08%20-%3E%20frw%0A%09x08%20-%3E%20frw%0A%09dvh%20-%3E%20z11%0A%09hnn%20-%3E%20z11%0A%09y35%20-%3E%20qvt%0A%09x35%20-%3E%20qvt%0A%09qvj%20-%3E%20fps%0A%09qvt%20-%3E%20fps%0A%09x30%20-%3E%20qqp%0A%09y30%20-%3E%20qqp%0A%09nwb%20-%3E%20vgr%0A%09dmf%20-%3E%20vgr%0A%09x31%20-%3E%20ctw%0A%09y31%20-%3E%20ctw%0A%09kvg%20-%3E%20kbg%0A%09hhf%20-%3E%20kbg%0A%09sbf%20-%3E%20z34%0A%09ngd%20-%3E%20z34%0A%09mjp%20-%3E%20jww%0A%09jcd%20-%3E%20jww%0A%09srm%20-%3E%20z10%0A%09kvh%20-%3E%20z10%0A%09y15%20-%3E%20ctg%0A%09x15%20-%3E%20ctg%0A%09y34%20-%3E%20ngd%0A%09x34%20-%3E%20ngd%0A%09bvk%20-%3E%20z38%0A%09trm%20-%3E%20z38%0A%09dmh%20-%3E%20dtf%0A%09bmm%20-%3E%20dtf%0A%09x20%20-%3E%20gjs%0A%09y20%20-%3E%20gjs%0A%09y26%20-%3E%20dsw%0A%09x26%20-%3E%20dsw%0A%09y04%20-%3E%20jqp%0A%09x04%20-%3E%20jqp%0A%09cjs%20-%3E%20kfq%0A%09gnb%20-%3E%20kfq%0A%09rtg%20-%3E%20z01%0A%09drq%20-%3E%20z01%0A%09ngk%20-%3E%20jbg%0A%09jcs%20-%3E%20jbg%0A%09ktf%20-%3E%20sqm%0A%09vpn%20-%3E%20sqm%0A%09nhs%20-%3E%20hjm%0A%09stn%20-%3E%20hjm%0A%09y37%20-%3E%20fmk%0A%09x37%20-%3E%20fmk%0A%09y13%20-%3E%20rmq%0A%09x13%20-%3E%20rmq%0A%09dsw%20-%3E%20dbd%0A%09ntc%20-%3E%20dbd%0A%09hwk%20-%3E%20z25%0A%09cbc%20-%3E%20z25%0A%09fgk%20-%3E%20z07%0A%09sqm%20-%3E%20z07%0A%09y28%20-%3E%20hwb%0A%09x28%20-%3E%20hwb%0A%09x11%20-%3E%20nvc%0A%09y11%20-%3E%20nvc%0A%09mst%20-%3E%20hrv%0A%09mgr%20-%3E%20hrv%0A%09wbm%20-%3E%20z03%0A%09hrv%20-%3E%20z03%0A%09gps%20-%3E%20z35%0A%09ggb%20-%3E%20z35%0A%09mbg%20-%3E%20tkf%0A%09djc%20-%3E%20tkf%0A%09y20%20-%3E%20nhf%0A%09x20%20-%3E%20nhf%0A%09rdf%20-%3E%20tgr%0A%09nck%20-%3E%20tgr%0A%09fps%20-%3E%20z36%0A%09rbf%20-%3E%20z36%0A%09x15%20-%3E%20rpb%0A%09y15%20-%3E%20rpb%0A%09sqh%20-%3E%20wmb%0A%09rpb%20-%3E%20wmb%0A%09spv%20-%3E%20sbf%0A%09hvw%20-%3E%20sbf%0A%09y18%20-%3E%20spp%0A%09x18%20-%3E%20spp%0A%09rww%20-%3E%20wdw%0A%09kbg%20-%3E%20wdw%0A%09fpv%20-%3E%20ptt%0A%09fjg%20-%3E%20ptt%0A%09x40%20-%3E%20mfj%0A%09y40%20-%3E%20mfj%0A%09y07%20-%3E%20fgk%0A%09x07%20-%3E%20fgk%0A%09y06%20-%3E%20vpn%0A%09x06%20-%3E%20vpn%0A%09x22%20-%3E%20cbv%0A%09y22%20-%3E%20cbv%0A%09stf%20-%3E%20cbc%0A%09djv%20-%3E%20cbc%0A%09x38%20-%3E%20hhv%0A%09y38%20-%3E%20hhv%0A%09hhm%20-%3E%20fkm%0A%09dqd%20-%3E%20fkm%0A%09frw%20-%3E%20z08%0A%09tkf%20-%3E%20z08%0A%09x37%20-%3E%20dvv%0A%09y37%20-%3E%20dvv%0A%09qrk%20-%3E%20tdr%0A%09rmq%20-%3E%20tdr%0A%09x35%20-%3E%20ggb%0A%09y35%20-%3E%20ggb%0A%09sbt%20-%3E%20qms%0A%09ndc%20-%3E%20qms%0A%09x21%20-%3E%20cpj%0A%09y21%20-%3E%20cpj%0A%09cbv%20-%3E%20z22%0A%09cmt%20-%3E%20z22%0A%09nrt%20-%3E%20nrq%0A%09trg%20-%3E%20nrq%0A%09btp%20-%3E%20mst%0A%09nhg%20-%3E%20mst%0A%09ksc%20-%3E%20gps%0A%09krw%20-%3E%20gps%0A%09x25%20-%3E%20hwk%0A%09y25%20-%3E%20hwk%0A%09fps%20-%3E%20vsq%0A%09rbf%20-%3E%20vsq%0A%09x39%20-%3E%20bbk%0A%09y39%20-%3E%20bbk%0A%09btp%20-%3E%20z02%0A%09nhg%20-%3E%20z02%0A%09x41%20-%3E%20twb%0A%09y41%20-%3E%20twb%0A%09sjb%20-%3E%20z27%0A%09dbd%20-%3E%20z27%0A%09sbn%20-%3E%20z26%0A%09cmn%20-%3E%20z26%0A%09cfp%20-%3E%20z37%0A%09dvv%20-%3E%20z37%0A%09djk%20-%3E%20nsp%0A%09jww%20-%3E%20nsp%0A%09x38%20-%3E%20bvk%0A%09y38%20-%3E%20bvk%0A%7D%0A