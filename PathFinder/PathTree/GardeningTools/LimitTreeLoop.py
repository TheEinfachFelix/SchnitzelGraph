from typing import List, Optional
from Path import FPath
from PathTree.TreeNode import TreeNode

def limitTreeLoop(oldRoot: TreeNode, endNodes: List[str], maxLoop: int) -> Optional[TreeNode]:
    
    def algo(node: TreeNode, backlog: List[str]) -> Optional[TreeNode]:
        if node.val in backlog:
            print("Loop detected:", node.val, backlog)
            return None
        
        new_backlog = backlog + [node.val]
        if len(new_backlog) > maxLoop:
            new_backlog.pop(0)

        new_node = TreeNode(node.val)

        for child in node.children:
            result = algo(child, new_backlog)
            if result:
                new_node.add_child(result)

        if not new_node.children and new_node.val not in endNodes:
            print("Pruned node:", new_node.val)
            return None
        return new_node
    return algo(oldRoot, [])
