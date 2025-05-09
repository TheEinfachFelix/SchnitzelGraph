import time
import networkx as nx
from PrettyPrint import PrettyPrintTree
from PathFinder.PathFinder import *


def main():

    # init Utils
    start = time.time()
    pt = PrettyPrintTree(lambda x: x.children, lambda x: x.val, orientation=PrettyPrintTree.Horizontal)

    # init Example Graph
    G = nx.Graph()
    elist = [('a', 'b', 5.0),('a', 'a', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0),('c', 'a', 1.0), ('c', 'd', 7.3),('a', 'd', 7.3)]
    G.add_weighted_edges_from(elist)
    StartNodes = ['a']
    EndNodes = ['d']


    print(f'Setup: {time.time() - start} Sekunden');start = time.time()
    # Start PathFinder
    print('Start PathFinder')
    tree = genPathTree(G, StartNodes, EndNodes, 7)
    print(f'Graph to TreeTree: {time.time() - start} Sekunden');start = time.time()

    # Filter Paths
    tree = limitPathListLength(tree, 0, 5, EndNodes)
    tree = limitPathListWeight(tree, 0, 10, EndNodes)
    tree = limitTreeLoop(tree, EndNodes,2)

    print(f'Filter: {time.time() - start} Sekunden');start = time.time()
    # Print Tree
    pt(tree)
    print(f'Print: {time.time() - start} Sekunden');start = time.time()

    # Print Paths
    paths = TreeToPath(tree)
    paths = sortPaths(paths)
    for path in paths:
        print(path)

    print(f'toPath: {time.time() - start} Sekunden');start = time.time()

    return (G, paths)

if __name__ == "__main__":
    main()