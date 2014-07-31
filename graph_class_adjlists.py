class Graph(object):
    def __init__(self):
        self.graph = {}
        
    def add_node(self, node):
        self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            add_node(node1)
        if node2 not in self.graph:
            add_node(node2)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def nodes(self):
        return self.graph.keys()

    def edges(self):
        graph = self.graph
        tups = [(node, adj_node) for node in graph for adj_node in graph[node]]
        return set([set(tup) for tup in tups])

class DiGraph(Graph):
    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            add_node(node1)
        if node2 not in self.graph:
            add_node(node2)
        self.graph[node1].append(node2)

    def edges(self):
        graph = self.graph
        return [(node, adj_node) for node in graph for adj_node in graph[node]]

