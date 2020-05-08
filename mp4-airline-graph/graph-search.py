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

    def dfs(self, s, e):

        path = []
        visited = set()

        def dfs_helper(v):
            if v == e:
                return True

            visited.add(v)

            for edge in self.adj(v):
                if edge.b not in visited:
                    path.append(edge)
                    if dfs_helper(edge.b):
                        return True

            return False

        return (dfs_helper(s), len(path), path)

    # We add our current node/vertex to visited -- time: 7.6us
    def bfs(self, s, e):

        path = []
        visited = set([s])
        queue = list(self.adj(s))

        while(queue):

            edge = queue.pop(0)

            if edge.b == e:
                path.append(edge)
                return (True, len(path), path)

            if edge.b not in visited:
                path.append(edge)
                visited.add(edge.b)
                queue.extend(self.adj(edge.b))

        return (False, len(path), path)

    # We add our child notes to the visited list  -- time: 6.8us
    def bfs2(self, s, e):
        if s == e:
            return True

        path = []
        queue = list(self.adj(s))
        visited = set([s, *map(lambda x: x.b, queue)])

        while(queue):
            edge = queue.pop(0)
            path.append(edge)

            if edge.b == e:
                return (True, len(path), path)

            for edge in self.adj(edge.b):
                if edge.b not in visited:
                    visited.add(edge.b)
                    queue.append(edge)

        return (False, len(path), path)

    def __str__(self):
        return "\n".join([str(k) + ": " + str(self.graph[k]) for k in self.graph.keys()])


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

print(g)
print("Vertices:", g.V, " Edges:", g.E, " Weight:", g.total_weight(), "\n", sep="")

s, e = ("b", "g")

print(g.dfs(s, e))
print(g.bfs(s, e))
print(g.bfs2(s, e))
