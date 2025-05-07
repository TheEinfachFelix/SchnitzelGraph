from PathFinder.PathFinder import TreeNode

def limitPathListWeight(root: TreeNode, minWeight: float, maxWeight: float, EndNodes: set, currentWeight: float = 0.0) -> TreeNode | None:
    new_root = TreeNode(root.val, 0.0)

    for child in root.children:
        weight = child.get_weight()
        newWeight = currentWeight + weight

        if newWeight > maxWeight:
            continue  # zu schwer, ignoriere diesen Pfad

        # rekursiver Aufruf auf Kindknoten
        new_child = limitPathListWeight(child, minWeight, maxWeight, EndNodes, newWeight)

        # Bedingung 1: Subtree ist gültig
        if new_child:
            new_root.children.append(new_child)

        # Bedingung 2: Kind ist ein EndNode und Gewicht ist im erlaubten Bereich
        elif child.val in EndNodes and minWeight <= newWeight <= maxWeight:
            copy_child = TreeNode(child.val)
            new_root.children.append(copy_child)

    if not new_root.children and (root.val not in EndNodes or currentWeight < minWeight):
        return None  # dieser Pfad ist unbrauchbar

    return new_root