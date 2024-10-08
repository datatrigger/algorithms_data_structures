# Correctness of approach 2 (Dijkstra)

TL;DR

The problem is represented as a weighted directed graph where each node corresponds to a *point of interest* (start position, key, lock) and a *state* (set of keys already collected). With (start node, 0 key) as the source node, consider $S$, the set of lengths of the shortest path**s** to the nodes with all keys. Then the question is about finding the minimum of *S*. Since Dijkstra finds shortest paths in nondecreasing order, then the "first time" it finds the shortest path to any node with all keys, it will necessarily be the minimum of S.

## Notations

$n$: number of distinct keys

In this solution, only the *points of interest* and *states* are considered. The *points of interest* are denoted $\{S, K_1, ... \, , K_n, L_1, ... \, ,L_n\}$ for the **S**tart position, **K**ey $1$ through $n$ and **L**ock $1$ through $n$. A *state* is the set of keys already picked up, represented as an element of $\{0, 1\}^{n}$ (and implemented as a bitmask).

$0_n$ denotes the n-tuple $(0, 0, ..., 0)$.  
$1_n$ denotes the n-tuple $(1, 1, ..., 1)$.

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

Assume that we are at a point in Dijkstra's algorithm where we have just processed vertex $v$, meaning $v$ has been added to the set of visited nodes, $V$, and its shortest path distance from the source, $d_v$, has been finalized. Now, we pop the next unvisited vertex $u$ from the priority queue with distance $d_u$. We aim to show that $d_u \geq d_v$.

##### Case 1: $u$ is a neighbor of $v$

In this case, vertex $u$ was either discovered or its tentative distance was updated when processing $v$. Let's denote the weight of the edge $v \rightarrow u$ by $w_{vu}$. When $u$ was discovered/updated, its tentative distance was set to:

$$d_u = d_v + w_{vu}$$

Since edge weights in Dijkstra's algorithm are assumed to be non-negative (i.e., $w_{vu} \geq 0$), we have:

$$d_u = d_v + w_{vu} \geq d_v$$

Thus, $d_u \geq d_v$ holds in this case.

##### Case 2: $u$ was already in the priority queue before processing $v$

In this case, vertex $u$ was in the priority queue with some tentative distance $d_u$ prior to processing $v$. Since Dijkstra’s algorithm processes vertices in order of increasing distance from the source, and $v$ was processed before $u$, it must be that:

$$d_v \leq d_u$$

Otherwise, $u$ would have been popped from the priority queue before $v$, contradicting the fact that $v$ was processed first. Therefore, in this case as well, $d_u \geq d_v$.

##### Conclusion:

In both cases, we have shown that $d_u \geq d_v$ when $u$ is popped from the priority queue immediately after processing $v$. Since this reasoning applies to every pair of consecutive vertices processed by Dijkstra's algorithm, it follows that the sequence of shortest path distances, as vertices are processed, is nondecreasing.

### 2) On-the-fly expansion

According to the previous section, we do not need to determine the shortest path distance for all nodes. The search can be stopped as soon as Dijkstra's algorithm processes any node with state $1_n$ i.e. "all the keys collected": since the distances are computed in nondecreasing order, this node's shortest distance is guaranteed to be the solution.

 This allows for a second optimization: instead of constructing the entire graph beforehand, we can generate it during the search only as needed.

# Code

