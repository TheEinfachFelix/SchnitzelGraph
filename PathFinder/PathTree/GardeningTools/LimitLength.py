from PathTree.TreeNode import TreeNode

def limitPathListLength(root: TreeNode, minLen: float, maxLen: float, EndNodes: set, currentLen: int = 0) -> TreeNode | None:
    new_root = TreeNode(root.val, 0.0)

    for child in root.children:
        newLen = currentLen + 1

        if newLen > maxLen:
            continue  # zu schwer, ignoriere diesen Pfad

        # rekursiver Aufruf auf Kindknoten
        new_child = limitPathListLength(child, minLen, maxLen, EndNodes, newLen)

        # Bedingung 1: Subtree ist gültig
        if new_child:
            new_root.children.append(new_child)

        # Bedingung 2: Kind ist ein EndNode und Gewicht ist im erlaubten Bereich
        elif child.val in EndNodes and minLen <= newLen <= maxLen:
            copy_child = TreeNode(child.val)
            new_root.children.append(copy_child)

    if not new_root.children and (root.val not in EndNodes or currentLen < minLen):
        return None  # dieser Pfad ist unbrauchbar

    return new_root