import time
import networkx as nx
from PrettyPrint import PrettyPrintTree
from PathFinder.PathFinder import *

pt = PrettyPrintTree(lambda x: x.children, lambda x: x.val, orientation=PrettyPrintTree.Horizontal)

start = time.time()

G = nx.Graph()
elist = [('a', 'b', 5.0),('a', 'a', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0),('c', 'a', 1.0), ('c', 'd', 7.3),('a', 'd', 7.3)]
G.add_weighted_edges_from(elist)

StartNodes = ['a']
EndNodes = ['d']


print(f'Init: {time.time() - start} Sekunden');start = time.time()

tree = genPathTree(G, StartNodes, EndNodes, 7)

print(f'Gen Tree: {time.time() - start} Sekunden');start = time.time()
#pt(tree)
tree = limitPathListLength(tree, 0, 5, EndNodes)
tree = limitPathListWeight(tree, 0, 10, EndNodes)
tree = limitTreeLoop(tree, EndNodes,2)

print(f'Filter: {time.time() - start} Sekunden');start = time.time()

pt(tree)

print(f'Print: {time.time() - start} Sekunden');start = time.time()

paths = pathToTree(tree)
for path in paths:
    print(path)


# TODO:
# sort by difference