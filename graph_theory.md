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

*Intuition*

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

For 2).