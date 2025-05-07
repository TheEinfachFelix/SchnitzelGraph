import networkx as nx
import AllPath
import PathSelector
from PrettyPrint import PrettyPrintTree
from PathTree.PathTreeGen import genPathTree
from PathTree.GardeningTools.LimitTreeLoop import *
from PathTree.GardeningTools.LimitWeight import *
from PathTree.GardeningTools.LimitLength import *




pt = PrettyPrintTree(lambda x: x.children, lambda x: x.val, orientation=PrettyPrintTree.Horizontal)

G = nx.Graph()
elist = [('a', 'b', 5.0),('a', 'a', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0),('c', 'a', 1.0), ('c', 'd', 7.3),('a', 'd', 7.3)]
G.add_weighted_edges_from(elist)

StartNodes = ['a']
EndNodes = ['d']

tree = genPathTree(G, StartNodes, EndNodes, 7)
#pt(tree)
tree = limitPathListLength(tree, 0, 5, EndNodes)
tree = limitPathListWeight(tree, 0, 10, EndNodes)
tree = limitTreeLoop(tree, EndNodes,2)

pt(tree)


# TODO:
# sort by difference
# get end Nodes method