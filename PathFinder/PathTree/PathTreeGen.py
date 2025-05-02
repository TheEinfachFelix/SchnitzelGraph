from PathTree.TreeNode import TreeNode, find_depth
import networkx as nx

def genPathTree(G: nx.Graph, start_node: list[str], end_node: list[str], max_depth: int):
    tree = TreeNode("root")

    def dfs(current_node: TreeNode):
        if find_depth(tree,current_node) > max_depth:
            return False

        if current_node.val in end_node:
            return True

        out = False
        for neighbor in G.neighbors(current_node.val):
            next = TreeNode(neighbor)
            current_node.add_child(next)
            fond = dfs(next)
            # RM pathst that dont end in end_node
            if not fond:
                current_node.remove_child(next)
            out = out or fond
        return out

    for i in start_node:
        next = TreeNode(i)
        tree.add_child(next)
        dfs(next)

    return tree
