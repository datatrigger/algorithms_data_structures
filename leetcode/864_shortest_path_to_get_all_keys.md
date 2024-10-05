# Correctness of approach 2 (Dijkstra)

## Framework

In this approach, only the *points of interest* and *states* are considered.

The *points of interest* are denoted $\{S, K_1, ... \, , K_n, L_1, ... \, ,L_n\}$ for the start position, key $1$ through $n$ and lock $1$ through $n$. A *state* is the set of keys already picked up, represented as an element of $\{0, 1\}^{n}$ (implemented as a bitmask).

All the elements of the set $\{S, K_1, ... \, , K_n, L_1, ... \, ,L_n\} \times \{0, 1\}^{n}$ can be represented as nodes of a weighted directed graph. All the nodes are connected, except when the target node is a lock and the source node's state does not have the right key. When edge $u \rightarrow v$ exists, then the weight is the shortest distance between $u$'s and $v$'s points of interest (precomputed via BFS).

## Correctness

With this representation of the problem in mind, the question can be rephrased as follows: find the shortest path between the start node $(S, 0_n)$ and the subset of nodes $\bigcup\limits_{1 \leq i \leq n} (K_i, 1_n)$.