from PathFinder.PathTree.TreeNode import TreeNode, find_depth, find_path

def pathToTree(root: TreeNode) -> list[list[str]]:
    if not root.children:
        return [[root.val]]

    paths = []
    for child in root.children:
        for path in pathToTree(child):
            paths.append([root.val] + path)

    return paths