from collections import defaultdict
from itertools import compress
# Vertex == Node
# Edge == Road == Line == Connection

# e == edge
# v == vertex
# w == weight


class Edge:
    def __init__(self, v, w):
        self.v = v
        self.w = w

    def __str__(self):
        return "(v:" + str(self.v) + " w:" + str(self.w) + ")"

    def __repr__(self):
        return "(v:" + str(self.v) + " w:" + str(self.w) + ")"


class Digraph:
    def __init__(self, V=0):
        self.V = V
        self.E = 0
        self.graph = defaultdict(list)

    def addEdge(self, a, b, w=1):
        self.E += 1
        #self.V = max(a + 1, b + 1, self.V)
        self.graph[a].append(Edge(b, w))

    def adjacents(self, v):
        return self.graph[v]

    def __str__(self):
        return "\n".join([str(k) + ": " + str(self.graph[k]) for k in self.graph.keys()])

    def minDistance(self, dist, spt):

        # Initilaize minimum distance for next node
        min_index = -1
        shortest = float("inf")

        # Find vertex with with shortest disntace and not in spt
        for v in range(self.V):
            if dist[v] < shortest and spt[v] is False:
                shortest = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):

        # Set distance from every node to src == infinity
        dist = [float("inf")] * self.V
        # Set distance from src to itself to 0
        dist[src] = 0
        # Shortest path tree
        spt = [False] * self.V

        for _ in range(self.V):

            # u is always gonna be the src itself
            # idx 5 -> 5 is 0 as we set on line 62 -> dist[src] = 0
            u = self.minDistance(dist, spt)

            # we add u to our shortest path tree
            spt[u] = True

            # Update dist value of the adjacent vertices
            for edge in self.adjacents(u):
                v = edge.v
                w = edge.w
                if spt[v] is False and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w

        return dist


g = Digraph(5)


g.addEdge(1, 2, 10)
g.addEdge(2, 1, 10)

g.addEdge(1, 3, 6)
g.addEdge(3, 1, 6)

g.addEdge(2, 4, 8)
g.addEdge(4, 2, 8)

print("Graph:\n", g, "\n", sep="")

res = g.dijkstra(2)
print(res)
