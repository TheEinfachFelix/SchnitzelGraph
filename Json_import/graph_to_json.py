import networkx as nx
import json

def graph_to_json(G: nx.DiGraph, start_node=None, end_node=None):
    """give the graph and start and end note to create a json file"""

    nodes = list(G.nodes)
    node_index = {node: idx for idx, node in enumerate(nodes)}

    json_data = []
    for node in nodes:
        connections = [-1] * len(nodes)
        for _, target, weight in G.out_edges(node, data='weight'):
            connections[node_index[target]] = weight
        
        node_entry = {
            "Node": node,
            "Connections": connections
        }
        if node == start_node:
            node_entry["Start"] = True
        if node == end_node:
            node_entry["End"] = True
        json_data.append(node_entry)

    return json_data