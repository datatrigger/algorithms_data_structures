# Undirected graphs

## Vertex degrees & size

$$\sum_{v \in V} deg(v) = 2 \cdot |E|$$

## Max *size* of a graph

For undirected graphs, since $deg(v) \leq |V| - 1$, then the relation above gives:

$|E| \leq \frac{|V| \cdot (|V| - 1)}{2}$

For directed graphs, the factor $\frac{1}{2}$ can be removed.

The size is roughly the order squared in the "worst" case: $|E| = O(|V|²)$

## Connected graphs & cycles

The number $|V| - 1$ is important in terms of size.

1.  If $|E| < |V| - 1$, then the graph cannot be connected.
2. If $|E| > |V| - 1$, then the graph contains a cycle

A tree is:

* an acyclic connected graph
* a connected graph with size $|V - 1|$
* a graph in which there is exactly one path between any two vertices

Conversely, a tree necessarily has $|V - 1|$ edges.

### Intuition

For 1). To build any connected graph, each vertex must come with at least 1 edge to connect itself to the existing graph, except for the first one. E.g.: 1, 2-, 3--, 4-

<pre>
1
</pre>

<pre>
1-2
</pre>

<pre>
1  &ndash;  2
 \ 3 /
</pre>

<pre>
1  &ndash;  2 - 4
 \ 3 /
</pre>

That is at least |V| - 1 edges.

For 2). Let $G$ be an undirected graph with size $|V|$. The connected components of $G$ are denoted $G_i \,, 1 \leq i \leq C$. There must be a connected component $G_j$ such that the size of $G_j$ is at least its order. Otherwise $|E| = |E_1| + ... + |E_C| \leq |V_1| - 1 + ... + |V_C| - 1 = |V| - C < |V|$, contradiction. $G_j$ is connected with $|E_j| > |V_j| - 1$ edges. But it could be connected with only $|V_j| - 1$ edges as per point 1). Then an "unnecessary" edge must form a cycle in subgraph $G_j$.