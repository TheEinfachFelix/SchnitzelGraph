import json
from typing import List, Tuple
import os
from pathlib import Path
path = Path(__file__).resolve().parent / "json_import.json"
WeightedEdge = Tuple[str, str, float]
import networkx as nx

def json_to_weighted_edges(data: List[dict]) -> Tuple[List[WeightedEdge], str, str]:
    nodes = [entry["Node"] for entry in data]
    node_index_map = {i: node for i, node in enumerate(nodes)}

    edges: List[WeightedEdge] = []
    start_node = end_node = None

    for i, entry in enumerate(data):
        current_node = entry["Node"]
        if entry.get("Start"):
            start_node = current_node
        if entry.get("End"):
            end_node = current_node
        connections = entry["Connections"]
        for j, weight in enumerate(connections):
            if weight != -1:
                target_node = node_index_map[j]
                edges.append((current_node, target_node, float(weight)))

    return edges, start_node, end_node

def warp_Matrix():
    returnList = []
    elist  = []
    with open(f"{path}", "r") as file:
        json_data = json.load(file)
    edges, start, end = json_to_weighted_edges(json_data)
    print("Weighted Edges:")
    for edge in edges:
        print(edge)
        elist.append(edge)
    if start and end:
        print(f"\nStart Node: {start}")
        print(f"End Node: {end}")
    returnList.append(elist)
    returnList.append([start])
    returnList.append([end])
    print(returnList)
    return returnList

def create_graph():
    G = nx.DiGraph()
    wm = warp_Matrix()
    print(wm[0])
    G.add_weighted_edges_from(wm[0])
    return G

if __name__ == "__main__":
    graph = create_graph()
    print(graph)