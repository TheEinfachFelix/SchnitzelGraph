from typing import List
from Path import FPath
from PathTree.TreeNode import TreeNode, find_depth

def limitPathListWeight(pathList: List[FPath], minWeight, maxWeight):
    return [path for path in pathList if minWeight <= path.get_weight() <= maxWeight]

def limitPathListLength(pathList: List[FPath], minLength, maxLength):
    return [path for path in pathList if minLength <= path.get_length() <= maxLength]

def limitTreeLoop(oldRoot: TreeNode, endNodes:list[str], maxLoop):

    def algo(node: TreeNode, backlog:List[str], parent:TreeNode=None):

        
        if node.val in backlog:
            parent.remove_child(node)
            return



        
        if len(node.children) == 0 and node.val not in endNodes:
            parent.remove_child(node)
            return
        
        backlog.append(node.val)
        if len(backlog) > maxLoop:
            backlog.pop(0)

        for i in node.children:
            algo(i, backlog, node)


    algo(oldRoot, [])
    return oldRoot