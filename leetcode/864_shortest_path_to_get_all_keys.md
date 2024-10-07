# Correctness of approach 2 (Dijkstra)

TL;DR

The problem is represented as a weighted directed graph where each node corresponds to a *point of interest* (start position, key, lock) and a *state* (set of keys already collected). With (start node, 0 key) as the source node, consider $S$, the set of lengths of the shortest path**s** to the nodes with all keys. Then the question is about finding the minimum of *S*. Since Dijkstra finds shortest paths in nondecreasing order, then the "first time" it finds the shortest path to any node with all keys, it will necessarily be the minimum of S.

## Notations

$n$: number of distinct keys

In this solution, only the *points of interest* and *states* are considered. The *points of interest* are denoted $\{S, K_1, ... \, , K_n, L_1, ... \, ,L_n\}$ for the **S**tart position, **K**ey $1$ through $n$ and **L**ock $1$ through $n$. A *state* is the set of keys already picked up, represented as an element of $\{0, 1\}^{n}$ (and implemented as a bitmask).

$0_n$ denotes the n-tuple $(0, 0, ..., 0)$ and $1_n$ the n-tuple with only ones.

$s(v)$ is the shortest path from $(S, 0_n)$ to node $v$.

## Model


All the elements of the set $\{S, K_1, ... \, , K_n, L_1, ... \, ,L_n\} \times \{0, 1\}^{n}$ can be represented as nodes of a weighted directed graph. All the nodes are connected, except when the target node is a lock and the source node's state does not have the right key. When edge $u \rightarrow v$ exists, then the weight is the shortest distance between $u$'s and $v$'s points of interest (precomputed via BFS).

## Correctness

With this representation of the problem, the question is about finding the following distance:

$$\min_{v \, \in \, \{(K_i, \, 1_n) \, | \, 1 \leq i \leq n\}} s(v)$$ 

It is now clear why Dijkstra's algorithm is suited here. However, there are still a few points to clarify.

### 1) Early stopping

A naïve solution would be to run Dijkstra until all shortest paths to $(K_i, \, 1_n), \, 1 \leq i \leq n$ have been found (with potentially some shortest paths left to $+\infty$ if some nodes $(K_i, \, 1_n)$ are not reachable). Then just take the minimum of these values and there is your solution.

But we can take advantage of this key-property: *Dijkstra's algorithm outputs shortest paths from the source in nondecreasing order* (see the proof below). As a consequence, the first time the algorithm processes any node $(K_i, 1_n), 1 \leq i \leq n$, then it is guaranteed to be less or equal than all other shortest paths to $\{(K_j, 1_n) \, | \, 1 \leq j \leq n,  \, j \neq i \}$. In other words, it is the minimum we are looking for.

#### Proof

Let’s proceed with a proof by contradiction by assuming that the sequence of shortest path distances determined by Dijkstra’s algorithm is not nondecreasing. This implies that at some point in the algorithm, an unvisited node $u$ is popped from the priority queue, and its shortest path distance $d_u$ is less than the shortest path distance $d_v$ of a previously visited node $v$.

### 2) On-the-fly expansion

The previous point allows for a second optimization: instead of pre-generating the entire graph before running Dijkstra's algorithm, we can compute it during the search only as needed.

# Code

