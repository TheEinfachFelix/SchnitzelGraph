from typing import List, Optional
from Path import FPath
from PathTree.TreeNode import TreeNode
yxcdasd
def limitPathListWeight(pathList: List[FPath], minWeight, maxWeight):
    return [path for path in pathList if minWeight <= path.get_weight() <= maxWeight]
