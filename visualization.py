import networkx as nx
from pyvis.network import Network
import os
from itertools import pairwise
from copy import deepcopy

FOLDER = "graphs"
COLOR = "lightblue"
HIGHLIGHT_COLOR = "orange"

WeightedEdge = tuple[str, str, float]

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
    """Erstellt einen gerichteten und gewichteten Graphen mit der networkx-Bibliothek."""
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(edges)
    return graph


def get_pyvis_network(graph: nx.Graph, directed=True) -> Network:
    """Erstellt aus einem networkx-Graphen ein Pyvis-Network."""
    network = Network(directed=directed)
    network.from_nx(graph)
    return network


def style_pyvis_network(network: Network, color="lightblue") -> None:
    """Gibt den Kanten und Knoten in einem Pyvis-Network ein Styling."""
    for edge in network.edges:
        print(edge)
        edge["label"] = str(edge["width"])
        edge["font"] = {
            "color": "black",
            "background": "white",
            "strokeWidth": 2,
            "strokeColor": "white",
        }

    for node in network.nodes:
        node["color"] = color
        node["size"] = 20
        node["font"] = {
            "size": 16, 
            "vadjust": -35,
        }


def visualize_network(
        network: Network,
        path_to_highlight: list[str] = [],
        html_name: str = 'network.html', 
    ) -> None:
    """
    Erstellt eine Kopie eines Pyvis-Networks, visualisiert diese und erstellt eine HTML-Datei. 
    Es kann optional ein Pfad angegeben werden, der hervorgehoben wird.
    """
    network_copy = deepcopy(network)
    highlight_path(network_copy, path_to_highlight)

    os.makedirs(FOLDER, exist_ok=True)
    full_path = os.path.join(FOLDER, html_name)
    network_copy.save_graph(full_path)


def highlight_path(network: Network, path: list[str]) -> None:
    """Hebt einen Pfad durch ein Pyvis-Network hervor"""
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
        else:
            node["color"] = COLOR


def main() -> None:
    graph = get_directed_weighted_graph(EDGES)
    network = get_pyvis_network(graph)
    style_pyvis_network(network)
    visualize_network(network, path_to_highlight=PATH, html_name="test.html")


if __name__ == "__main__":
    main()
