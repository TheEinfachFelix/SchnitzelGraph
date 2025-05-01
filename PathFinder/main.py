import networkx as nx
import AllPath
import PathSelector

G = nx.Graph()
elist = [('a', 'b', 5.0),('a', 'a', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0),('c', 'a', 1.0), ('c', 'd', 7.3),('a', 'd', 7.3)]
G.add_weighted_edges_from(elist)

data = AllPath.AllPath(G, 'a', 'd',0.7, 11.3)
#data = PathSelector.limitPathListWeight(data, 0, 20)
#data = PathSelector.limitPathListLength(data, 0, 5)
#data = PathSelector.limitPathListLoop(data, 2)

for i in data:
    print(i)
print("Anzahl der Pfade: ", len(data))