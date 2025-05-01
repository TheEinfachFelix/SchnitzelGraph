import networkx as nx
import Path





def AllPath(G: nx.Graph, start_node: str, end_node: str, minCoverage: float, maxCoverage: float):
    valid_paths = []
    numberOfNodes = len(G.nodes)
    cutoff = int(numberOfNodes*maxCoverage)-1

    for path in nx.all_simple_paths(G, source=start_node, target=end_node, cutoff=cutoff):
        newPath = Path.FPath(path, G)
        if newPath.get_coverage() < minCoverage:
            print(f"Path {path} is too short, skipping.")
            continue

        valid_paths.append(newPath)

    return valid_paths
