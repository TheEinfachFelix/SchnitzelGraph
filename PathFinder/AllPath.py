import networkx as nx
import Path





def AllPath(G: nx.Graph, start_node: str, end_node: str) -> list:
    pahts = []
    for i in nx.all_simple_paths(G, source=start_node, target=end_node):
        pahts.append( Path.FPath(i, G))
    return pahts
