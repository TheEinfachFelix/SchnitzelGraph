import streamlit as st
import streamlit.components.v1 as components
import os

import visualization as vs

def start_streamlit():
    st.set_page_config(page_title="Schnitzelgraph", layout="wide")

    st.title("Visualisierung von Pfaden durch einen Graphen")

    network, paths = get_example_graph_and_paths()
    
    handle_graph_and_paths(network, paths)


def handle_graph_and_paths(network, paths):
    vs.style_pyvis_network(network)

    if st.button("Graph ohne Pfad"):
        generate_button_and_graph(network, [])

    for idx, path in enumerate(paths):
        if st.button(f"Highlight Pfad {idx+1}: {' ➔ '.join(path)}"):
            generate_button_and_graph(network, path)

def get_example_graph_and_paths():
    paths = [
        ["A", "B", "D", "H", "I", "J"],
        ["A", "C", "F", "G", "I"],
        ["B", "E", "H"]
    ]
    graph = vs.get_directed_weighted_graph(vs.EDGES)
    network = vs.get_pyvis_network(graph)
    return network, paths


def generate_button_and_graph(network, path):
    vs.visualize_network(network, path_to_highlight=path, html_name="highlighted_graph.html")
            
    highlight_html_path = os.path.join(vs.FOLDER, "highlighted_graph.html")
    with open(highlight_html_path, "r", encoding="utf-8") as f:
        highlight_html = f.read()

    components.html(highlight_html, height=600, scrolling=True)


def main():
    start_streamlit()


if __name__ == "__main__":
    main()