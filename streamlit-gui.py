import streamlit as st
import streamlit.components.v1 as components
import os

import visualization as vs
from pyvis.network import Network
from main import main


def start_streamlit() -> None:
    """
    Startet die Streamlit-Anwendung und konfiguriert die Benutzeroberfläche.
    Zeigt den Titel und initialisiert die Visualisierung des Graphen und der Pfade.
    """
    st.set_page_config(page_title="Schnitzelgraph", layout="wide")

    st.title("Visualisierung von Pfaden durch einen Graphen")

    network, paths = get_graph_and_path_from_main()
    
    handle_graph_and_paths(network, paths)


def handle_graph_and_paths(network: Network, paths: list[list[str]]) -> None:
    """
    Handhabt die Darstellung des Graphen und der Pfade.
    Stellt Buttons bereit, um den Graphen ohne Pfad oder mit hervorgehobenen Pfaden anzuzeigen.
    """
    vs.style_pyvis_network(network)

    if st.button("Graph ohne Pfad"):
        generate_button_and_graph(network, [])

    for idx, path in enumerate(paths):
        if st.button(f"Highlight Pfad {idx+1}: {' ➔ '.join(path)}"):
            generate_button_and_graph(network, path)


def get_example_graph_and_paths() -> tuple[Network, list[list[str]]]:
    """
    Erstellt ein Beispielgraphen und eine Liste von Beispielpfaden.
    """
    paths = [
        ["A", "B", "D", "H", "I", "J"],
        ["A", "C", "F", "G", "I"],
        ["B", "E", "H"]
    ]
    graph = vs.get_directed_weighted_graph(vs.EDGES)
    network = vs.get_pyvis_network(graph)
    return network, paths


def get_graph_and_path_from_main() -> tuple[Network, list[list[str]]]:
    """
    Ruft den Graphen und die Pfade aus der `main`-Funktion ab.
    """
    graph, paths = main()
    network = vs.get_pyvis_network(graph)
    return network, paths


def generate_button_and_graph(network: Network, path: list[str]) -> None:
    """
    Generiert die HTML-Darstellung des Graphen mit oder ohne hervorgehobenen Pfad
    und zeigt diese in der Streamlit-Anwendung an.
    """
    vs.visualize_network(network, path_to_highlight=path, html_name="highlighted_graph.html")
            
    highlight_html_path = os.path.join(vs.FOLDER, "highlighted_graph.html")
    with open(highlight_html_path, "r", encoding="utf-8") as f:
        highlight_html = f.read()

    components.html(highlight_html, height=600, scrolling=True)


if __name__ == "__main__":
    start_streamlit()