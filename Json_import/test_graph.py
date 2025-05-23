import matplotlib.pyplot as plt
import networkx as nx
from json_import_file import create_graph, warp_Matrix  

def visualize_graph():
    """visualise the json_import graph for testing"""
    G = create_graph()
    edges, start_node, end_node = warp_Matrix()

    pos = nx.spring_layout(G, seed=42)  # Positioning for visualization

    # Draw nodes
    node_colors = []
    for node in G.nodes:
        if node == start_node:
            node_colors.append("green")
        elif node == end_node:
            node_colors.append("red")
        else:
            node_colors.append("skyblue")

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)
    nx.draw_networkx_labels(G, pos, font_size=12)

    # Draw edges
    nx.draw_networkx_edges(G, pos, arrows=True)
    edge_labels = {(u, v): f"{d['weight']:.1f}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="gray")

    plt.title("Directed Graph Visualization")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_graph()