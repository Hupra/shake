from collections import defaultdict
from my_heapq import heapify, heappop
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


class Vertex:
    def __init__(self, v, d=float("inf")):
        self.v = v              # vertex
        self.d = d              # distance
        self.p = None           # parent, what node was used to get here

    def __lt__(self, other):
        return self.d < other.d

    def __repr__(self):
        return "|" + str(self.v) + " " + str(self.d) + "|"

    def print_path(self):
        s = "(" + str(self.v) + ")"
        node = self.p

        while(node is not None):
            s = "(" + str(node.v) + ")->" + s
            node = node.p

        print(s)
        print("-" * len(s))


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

    def dijkstra(self, s):

        # Add all of our other verticies to our priorityqueue
        pq = list(map(Vertex, self.known))

        # Add all our vertices to our dict
        d = {v.v: v for v in pq}

        # Set distance from s to s
        d[s].d = 0

        # Heapify our priority queue
        heapify(pq)

        while(pq):

            # Get the first element in our queue
            v = heappop(pq)

            # Look at each edge of the vortex
            for e in self.adj(v.v):

                # find the Vertex object of the target of the
                # current edge using our dict
                target_v = d[e.b]

                # if the distance to the target vertes is greater
                # than the distance to the current vertex + the
                # weight of the current edge, we update
                # the target vertex
                if v.d + e.w < target_v.d:
                    target_v.d = v.d + e.w  # Set new distance to the vertex
                    target_v.p = v          # Set new previous//parent

            heapify(pq)

        return d


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

start = "b"

for k, v in g.dijkstra(start).items():
    print(start + "--" + str(v.d) + "--" + str(k))
    v.print_path()

# ------------------------------------------------------------------------------------------------ #

g = Digraph()
g.addEdge(1, 2, 24)
g.addEdge(1, 2, 24)
g.addEdge(1, 4, 20)
g.addEdge(4, 1, 20)
g.addEdge(3, 1, 3)
g.addEdge(1, 3, 3)
g.addEdge(4, 3, 12)
g.addEdge(3, 4, 12)

s = 1

r = g.dijkstra(s)
d = {k: v.d for k, v in r.items()}
d = defaultdict(lambda: float("inf"), d)

n = 4
res = [d[x] if d[x] != float("inf") else -1 for x in range(1, n + 1) if d[x] > 0]
print("RES:", * res, sep=" ")
print("EXP: 24 3 15\n")


# ------------------------------------------------------------------------------------------------ #

g = Digraph()
g.addEdge(1, 2, 10)
g.addEdge(2, 1, 10)
g.addEdge(1, 3, 6)
g.addEdge(3, 1, 6)
g.addEdge(2, 4, 8)
g.addEdge(4, 2, 8)

s = 2

r = g.dijkstra(s)
d = {k: v.d for k, v in r.items()}
d = defaultdict(lambda: float("inf"), d)

n = 5
res = [d[x] if d[x] != float("inf") else -1 for x in range(1, n + 1) if d[x] > 0]
print("RES:", * res, sep=" ")
print("EXP: 10 16 8 -1\n")

# -----------------------------------------------------------------------------------------------#
# https://www.hackerrank.com/challenges/dijkstrashortreach/problem
# -----------------------------------------------------------------------------------------------#

# with open("input02.txt") as f:
#     txt = f.read()
# a = txt.split("\n")


# t = int(a.pop(0))  # number of cases

# for _ in range(t):
#     n, m = map(int, a.pop(0).split())  # nodes, edges

#     g = Digraph()

#     data = set(tuple(a.pop(0).split()) for _ in range(m))

#     for x in data:
#         x, y, z = map(int, x)
#         g.addEdge(x, y, z)
#         g.addEdge(y, x, z)

#     s = int(a.pop(0))

#     d = g.dijk(s)
#     d = {k: v.d for k, v in d.items()}
#     d = defaultdict(lambda: float("inf"), d)

#     exp = "3 6 4 5 5 4 5 4 3 3 4 6 6 4 4 4 4 5 3 4 5 3 4 6 8 4 5 3 4 4 5 4 6 6 2 4 6 4 4 4 4 5 5 3 4 5 3 6 5 4 5 5 4 4 5 3 3 4 2 3 5 2 4 4 3 4 10 5 5 7 4 4 4 1 4 4 4 5 4 4 5 4 4 5 4 5 6 5 4 4 5 5 5 4 4 4 4 3 4 5 3 3 5 4 6 8 2 5 3 4 4 5 3 5 3 3 4 5 3 6 5"
#     res = [d[x] if d[x] != float("inf") else -1 for x in range(1, n + 1) if d[x] > 0]

#     exp = list(map(int, exp.split()))
#     print(*res[:10], sep=" ")
#     print(*exp[:10], sep=" ")

# print("done")
