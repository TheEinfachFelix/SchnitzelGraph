from PathFinder.PathTree.TreeNode import TreeNode, find_depth, find_path
from difflib import SequenceMatcher

def TreeToPath(root: TreeNode) -> list[list[str]]:
    if not root.children:
        return [[root.val]]

    paths = []
    for child in root.children:
        for path in TreeToPath(child):
            paths.append([root.val] + path)

    return paths

def path_similarity(a: list[str], b: list[str]) -> float:
    # Gibt ein Ähnlichkeitsmaß zwischen 0 (komplett verschieden) und 1 (identisch)
    return SequenceMatcher(None, a, b).ratio()

def sortPaths(paths: list[list[str]]) -> list[list[str]]:
    scores = []
    for i, path in enumerate(paths):
        sim_sum = 0
        for j, other in enumerate(paths):
            if i != j:
                sim_sum += path_similarity(path, other)
        avg_sim = sim_sum / (len(paths) - 1)
        scores.append((avg_sim, path))
    
    # Sortieren nach aufsteigender Ähnlichkeit -> unterschiedlichere Pfade zuerst
    sorted_paths = sorted(scores, key=lambda x: x[0])
    return [path for _, path in sorted_paths]