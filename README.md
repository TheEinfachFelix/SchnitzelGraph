# SchnitzelGraph

**SchnitzelGraph** ist ein Python-Projekt zur Visualisierung und Analyse von Graphen, die aus geografischen Daten erstellt werden. Es verwendet Bibliotheken wie `networkx`, `pyvis` und `streamlit`, um interaktive Graphen zu generieren und Pfade hervorzuheben. Es soll zum Erstellen einer Schnitzeljagd genutzt werden.

## Funktionen

- **Import von Geodaten**: Liest geografische Daten aus einer CSV-Datei und erstellt einen Graphen basierend auf Entfernungen zwischen Punkten.
- **Visualisierung**: Stellt den Graphen interaktiv mit PyVis dar, einschließlich der Möglichkeit, bestimmte Pfade hervorzuheben.
- **Streamlit-GUI**: Eine benutzerfreundliche Oberfläche zur Anzeige und Interaktion mit dem Graphen.
- **Pfad-Highlighting**: Hebt bestimmte Pfade im Graphen hervor, basierend auf benutzerdefinierten Eingaben.

## Installation

1. **Voraussetzungen**:
   - Python 3.8 oder höher
   - Virtuelle Umgebung (empfohlen)

2. **Abhängigkeiten installieren**:
   ```bash
   pip install -r requirements.txt

3. **Projekt starten**:
   - Streamlit-GUI starten:
   ```bash
   streamlit run streamlit-gui.py
   ```
## Verwendung

### 1. CSV-Datei vorbereiten
Die CSV-Datei sollte die folgenden Spalten enthalten:
- `Name`: Der Name des Punktes.
- `WKT`: Die geografischen Koordinaten im WKT-Format, z. B. `POINT (lon lat)`.
- `Beschreibung` (optional): Eine Beschreibung des Punktes.

### 2. Graph erstellen
Die Funktion `MapToGraph` in `importmap.py` erstellt einen Graphen aus der CSV-Datei:
```python
from importmap import MapToGraph

graph = MapToGraph("daten.csv", max_distance=1000)
```

### 3. Visualisierung
Die Visualisierung erfolgt über die Streamlit-GUI:
- Starten Sie die Anwendung mit `streamlit run streamlit-gui.py`.
- Interagieren Sie mit dem Graphen und heben Sie Pfade hervor.

## Projektstruktur

```plaintext
SchnitzelGraph/
├── importmap.py         # Importiert Geodaten und erstellt einen Graphen
├── visualization.py     # Visualisiert den Graphen mit PyVis
├── streamlit-gui.py     # Streamlit-Anwendung für die Benutzeroberfläche
├── main.py              # Hauptlogik des Projekts
├── graphs/              # Ordner für generierte HTML-Dateien
├── requirements.txt     # Abhängigkeiten
└── README.md            # Projektbeschreibung
```

## Beispiele

### Beispiel-CSV-Datei
```csv
Name,WKT,Beschreibung
A,"POINT (10.0 50.0)","Startpunkt"
B,"POINT (10.1 50.1)","Zwischenpunkt"
C,"POINT (10.2 50.2)","Endpunkt"
```

### Beispielcode
```python
from importmap import MapToGraph
from visualization import visualize_network

graph = MapToGraph("daten.csv", max_distance=1000)
visualize_network(graph, path_to_highlight=["A", "B", "C"])
```

## Abhängigkeiten

- `networkx`: Erstellung und Analyse von Graphen.
- `pyvis`: Interaktive Visualisierung von Graphen.
- `streamlit`: Erstellung einer Web-GUI.
- `math` und `csv`: Verarbeitung von geografischen Daten.