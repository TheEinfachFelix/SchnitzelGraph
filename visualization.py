import networkx as nx
from pyvis.network import Network
from itertools import pairwise

WeightedEdge = tuple[str, str, float]

COLOR = "black"
HIGHLIGHT_COLOR = "orange"

EDGES: list[WeightedEdge] = [
    ("A", "B", 5),
    ("A", "C", 4),
    ("B", "D", 4),
    ("B", "E", 5),
    ("C", "D", 2),
    ("C", "F", 3),
    ("D", "H", 6),
    ("E", "H", 4),
    ("F", "G", 2),
    ("G", "F", 2),
    ("G", "I", 1),
    ("H", "I", 1),
    ("I", "J", 2),
    ("J", "I", 2)
]

PATH = ["A", "B", "D", "H", "I", "J"]

def get_directed_weighted_graph(edges: list[WeightedEdge]) -> nx.Graph:
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(edges)
    return graph


def get_pyvis_network(graph: nx.Graph, directed=True) -> Network:
    network = Network(directed=directed)
    network.from_nx(graph)
    return network


def visualize_network(network: Network, html_name: str = 'network.html') -> None:
    for edge in network.edges:
        edge["label"] = str(edge["width"])
        edge["font"] = {
            "color": "black",
            "background": "white",
            "strokeWidth": 2,
            "strokeColor": "white",
        }
    network.show(html_name, notebook=False)


def highlight_path(network: Network, path: list[str]) -> None:
    path_edges = list(pairwise(path))
    for edge in network.edges:
        if (edge["from"], edge["to"]) in path_edges:
            edge["color"] = HIGHLIGHT_COLOR
        else: 
            edge["color"] = COLOR
    
    for node in network.nodes:
        if node["id"] in path:
            node["color"] = HIGHLIGHT_COLOR
            node["size"] = 20
            node["font"] = {"size": 16, "vadjust": -30}
        else:
            node["color"] = COLOR


def main() -> None:
    graph = get_directed_weighted_graph(EDGES)
    network = get_pyvis_network(graph)
    highlight_path(network, PATH)
    visualize_network(network)


if __name__ == "__main__":
    main()
