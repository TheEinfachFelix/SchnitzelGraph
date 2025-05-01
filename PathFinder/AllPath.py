import networkx as nx
from Path import FPath





def AllPath(G: nx.Graph, start_node: str, end_node: str, minCoverage: float, maxDoubels: float, max_depth: int = 10):
    valid_paths = []

    def dfs(current_path: FPath):
        current_node = current_path.get_path()[-1]       

        # Abbruchbedingung
        if len(current_path.get_path()) > max_depth:
            return

        if current_node == end_node:
            if minCoverage <= current_path.get_coverage() and current_path.get_doubels() <= maxDoubels:
                # deepcopy nicht nötig, da wir bei Backtracking immer neuen Pfadstand erzeugen
                valid_paths.append(FPath(list(current_path.get_path()), G))
            return

        for neighbor in G.neighbors(current_node):
            current_path.add_node(neighbor)

            #if current_path.get_doubels() <= maxDoubels:
            dfs(current_path)
            current_path.pop_node()

    dfs(FPath([start_node], G))
    return valid_paths
