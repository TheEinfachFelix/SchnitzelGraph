from PathFinder.PathTree.TreeNode import TreeNode, find_depth, find_path
import networkx as nx

def genPathTree(G: nx.Graph, start_node: list[str], end_node: list[str], max_depth: int):
    tree = TreeNode("root", 0.0)

    def dfs(current_node: TreeNode):
        if find_depth(tree, current_node) > max_depth:
            return False

        if current_node.val in end_node:
            return True

        out = False
        for neighbor in G.neighbors(current_node.val):
            weight = G[current_node.val][neighbor].get("weight", 1.0)
            next = TreeNode(neighbor, weight)
            current_node.add_child(next)
            found = dfs(next)

            if not found:
                current_node.remove_child(next)
            out = out or found
        return out

    for i in start_node:
        next = TreeNode(i, 0.0)  # Startknoten haben Gewicht 0
        tree.add_child(next)
        dfs(next)

    return tree