from collections import defaultdict
# Vertex == Node
# Edge == Road == Line == Connection

# e == edge
# v == vertex
# w == weight


class Edge:
    def __init__(self, a, b, w=1):
        self.a = a
        self.b = b
        self.w = w

    def __lt__(self, other):
        return self.w < other.w

    def __hash__(self):
        return hash(tuple(self))

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.w == other.w

    def __str__(self):
        return str(self.a) + "--" + str(self.w) + "--" + str(self.b)

    def __repr__(self):
        return str(self.a) + "--" + str(self.w) + "--" + str(self.b)

    def __iter__(self):
        for att in self.__dict__.keys():
            yield self.__getattribute__(att)


class Digraph:

    def __init__(self, edges=[]):
        self.E = 0
        self.known = set()
        self.graph = defaultdict(set)
        for edge in edges:
            self.addEdge(*edge)

    @property
    def V(self):
        return len(self.known)

    def addEdge(self, a, b, w=1):
        self.E += 1

        self.known.add(a)
        self.known.add(b)

        self.graph[a].add(Edge(a, b, w))

    def adj(self, v):
        return self.graph[v]

    def vers(self):
        return list(self.graph.keys())

    def total_weight(self):
        return sum([edge.w for v in self.vers() for edge in self.adj(v)])

    def __str__(self):
        return "\n".join([str(k) + ": " + str(self.graph[k]) for k in self.graph.keys()])

    def relax(self, dist, spt):

        min_key = None
        shortest = float("inf")

        for k, v in dist.items():
            if v < shortest and spt[k] is False:
                shortest = v
                min_key = k

        return min_key

    def dijkstra(self, src):

        spt = defaultdict(bool)
        dist = defaultdict(lambda: float("inf"))
        dist[src] = 0

        for _ in range(self.V):

            u = self.relax(dist, spt)

            spt[u] = True

            for edge in self.adj(u):
                v = edge.b
                w = edge.w

                if spt[v] is False and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w

        return dist


g = Digraph()
g.addEdge("a", "b", 2)
g.addEdge("a", "c", 3)
g.addEdge("a", "d", 3)
g.addEdge("b", "a", 2)
g.addEdge("b", "c", 4)
g.addEdge("b", "e", 3)
g.addEdge("c", "a", 3)
g.addEdge("c", "b", 4)
g.addEdge("c", "d", 5)
g.addEdge("c", "e", 1)
g.addEdge("c", "f", 6)
g.addEdge("d", "a", 3)
g.addEdge("d", "c", 5)
g.addEdge("d", "f", 7)
g.addEdge("e", "b", 3)
g.addEdge("e", "c", 1)
g.addEdge("e", "f", 8)
g.addEdge("f", "c", 6)
g.addEdge("f", "d", 7)
g.addEdge("f", "e", 8)
g.addEdge("f", "g", 9)
g.addEdge("g", "f", 9)


print(g, "\n")

src = "b"

res = g.dijkstra(src)

for k, v in res.items():
    print(str(src) + "--" + str(v) + "--" + str(k))

# n = 4
# res = [res[x] if res[x] != float("inf") else -1 for x in range(1, n + 1) if res[x] > 0]
# print(*res, sep=" ")
