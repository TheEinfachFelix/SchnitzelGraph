import streamlit as st
import streamlit.components.v1 as components
import os

import visualization as vs

PATHS = [
    ["A", "B", "D", "H", "I", "J"],
    ["A", "C", "F", "G", "I"],
    ["B", "E", "H"]
]

st.set_page_config(page_title="Schnitzelgraph", layout="wide")

st.title("Visualisierung von Pfaden durch einen Graphen")

graph = vs.get_directed_weighted_graph(vs.EDGES)
network = vs.get_pyvis_network(graph)
vs.style_pyvis_network(network)
vs.visualize_network(network, path_to_highlight=[], html_name="base_graph.html")

html_path = os.path.join(vs.FOLDER, "base_graph.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_data = f.read()

components.html(html_data, height=600, scrolling=True)

st.header("Mögliche Pfade")

for idx, path in enumerate(PATHS):
    if st.button(f"Highlight Pfad {idx+1}: {' ➔ '.join(path)}"):
        vs.visualize_network(network, path_to_highlight=path, html_name="highlighted_graph.html")
        
        highlight_html_path = os.path.join(vs.FOLDER, "highlighted_graph.html")
        with open(highlight_html_path, "r", encoding="utf-8") as f:
            highlight_html = f.read()

        components.html(highlight_html, height=600, scrolling=True)