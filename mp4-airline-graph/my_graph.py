from collections import defaultdict
from my_heapq import heapify, heappop
from functools import reduce
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
        self.p = None           # parent -> what node was used to get here

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
        return self.known

    def edges(self):
        return sum(map(list, self.graph.values()), [])

    def total_weight(self):
        return sum(map(lambda e: e.w, self.edges()))

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

    @staticmethod
    def simple_graph():
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
        return g
