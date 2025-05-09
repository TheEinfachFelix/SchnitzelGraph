import networkx as nx

class FPath:
    def __init__(self, path: list, graph: nx.Graph):
        self.path = path
        self.graph = graph

    def get_path(self):
        return self.path
    def get_weight(self):
        return sum([self.graph[u][v]['weight'] for u, v in zip(self.path[:-1], self.path[1:])])
    def get_length(self):
        return len(self.path)
    def get_doubels(self):
        return len(self.path) / len(set(self.path))
    def get_coverage(self):
        return len(set(self.path)) / len(self.graph.nodes)
    def add_node(self, node: str):
        self.path.append(node)
    def pop_node(self):
        self.path.pop()
    
    def __str__(self):
        return f"Path: {self.path}, Weight: {self.get_weight()}, Length: {self.get_length()}"