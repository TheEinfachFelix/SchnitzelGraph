from typing import List

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        return child
    def remove_child(self, child):
        self.children.remove(child)
        return child

def find_depth(root, target, current_depth=0):
    if root is target:
        return current_depth

    for child in root.children:
        depth = find_depth(child, target, current_depth + 1)
        if depth != -1:
            return depth

    return -1

def find_path(root, target):
    if root is target:
        return [root]

    for child in root.children:
        path = find_path(child, target)
        if path:
            return [root] + path

    return []  # kein Pfad gefunden