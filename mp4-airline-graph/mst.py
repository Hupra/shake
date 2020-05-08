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

    def __str__(self):
        return str(self.a) + "--" + str(self.w) + "->" + str(self.b)

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

        if a not in self.known:
            self.known.add(a)

        if b not in self.known:
            self.known.add(b)

        self.graph[a].add(Edge(a, b, w))

    def adj(self, v):
        return self.graph[v]

    def vers(self):
        return list(self.graph.keys())

    def total_weight(self):
        return sum([edge.w for v in self.vers() for edge in self.adj(v)])

    def mst(self, s):

        mst = Digraph()

        visited = set([s])
        edges = set(self.adj(s))

        while(edges):

            sel = min(edges)
            edges = set(filter(lambda e: e.b != sel.b, edges))

            if sel.b not in visited:
                visited.add(sel.b)
                mst.addEdge(*sel)

                for edge in self.adj(sel.b):
                    if edge.b not in visited:
                        edges.add(edge)

        return mst

    def __str__(self):
        return "\n".join([str(k) + ": " + str(self.graph[k]) for k in self.graph.keys()])


g = Digraph()
g.addEdge("A", "B", 2)
g.addEdge("A", "C", 3)
g.addEdge("A", "D", 3)
g.addEdge("B", "A", 2)
g.addEdge("B", "C", 4)
g.addEdge("B", "E", 3)
g.addEdge("C", "A", 3)
g.addEdge("C", "B", 4)
g.addEdge("C", "D", 5)
g.addEdge("C", "E", 1)
g.addEdge("C", "F", 6)
g.addEdge("D", "A", 3)
g.addEdge("D", "C", 5)
g.addEdge("D", "F", 7)
g.addEdge("E", "B", 3)
g.addEdge("E", "C", 1)
g.addEdge("E", "F", 8)
g.addEdge("F", "C", 6)
g.addEdge("F", "D", 7)
g.addEdge("F", "E", 8)
g.addEdge("F", "G", 9)
g.addEdge("G", "F", 9)

print(g)
print("Vertices:", g.V, " Edges:", g.E, " Weight:", g.total_weight(), "\n", sep="")

mst = g.mst("A")
print(mst)
print("Vertices:", mst.V, " Edges:", mst.E, " Weight:", mst.total_weight(), "\n", sep="")

#
# For more info:
# https://www.youtube.com/watch?v=cplfcGZmX7I
#
