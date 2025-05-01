import networkx as nx
import AllPath

G = nx.Graph()
elist = [('a', 'b', 5.0),('a', 'a', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0),('c', 'a', 1.0), ('c', 'd', 7.3),('a', 'd', 7.3)]
G.add_weighted_edges_from(elist)

for i in AllPath.AllPath(G, 'a', 'd',0,10):
    print(i)