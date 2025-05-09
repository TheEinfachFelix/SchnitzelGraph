import csv
import math
import networkx as nx
import matplotlib.pyplot as plt

def haversine(lat1, lon1, lat2, lon2):
   R = 6371000  # Erdradius in Metern
   phi1 = math.radians(lat1)
   phi2 = math.radians(lat2)
   dphi = math.radians(lat2 - lat1)
   dlambda = math.radians(lon2 - lon1)
   a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
   c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
   return R * c
def parse_point_wkt(wkt):
   wkt = wkt.replace("POINT (", "").replace(")", "")
   lon_str, lat_str = wkt.strip().split()
   return float(lat_str), float(lon_str)
def build_graph_with_distance_limit(csv_path, max_distance):
   G = nx.Graph()
   nodes = []
   # 1. Knoten einlesen
   with open(csv_path, newline='', encoding='utf-8') as file:
       reader = csv.DictReader(file)
       for row in reader:
           name = row['Name']
           beschreibung = row.get('Beschreibung', '')
           lat, lon = parse_point_wkt(row['WKT'])
           G.add_node(name, beschreibung=beschreibung, lat=lat, lon=lon)
           nodes.append((name, lat, lon))
   # 2. Kanten mit Distanz ≤ max_distance hinzufügen
   for i, (name1, lat1, lon1) in enumerate(nodes):
       for j in range(i + 1, len(nodes)):
           name2, lat2, lon2 = nodes[j]
           dist = haversine(lat1, lon1, lat2, lon2)
           if dist <= max_distance:
               G.add_edge(name1, name2, weight=dist)
   # 3. Sicherstellen, dass jeder Knoten mindestens einen Nachbarn hat
   for i, (name1, lat1, lon1) in enumerate(nodes):
       if G.degree(name1) == 0:
           # Finde den nächsten Knoten (egal wie weit entfernt)
           min_dist = float("inf")
           nearest_node = None
           for j, (name2, lat2, lon2) in enumerate(nodes):
               if name1 == name2:
                   continue
               dist = haversine(lat1, lon1, lat2, lon2)
               if dist < min_dist:
                   min_dist = dist
                   nearest_node = name2
           # Verbindung hinzufügen
           G.add_edge(name1, nearest_node, weight=min_dist)
   return G

# Distanzlimit in Metern (frei wählbar)
MAX_DISTANZ = 70000
# Graph erzeugen
graph = build_graph_with_distance_limit("nodes.csv", max_distance=MAX_DISTANZ)
# Knotenpositionen extrahieren (Längengrad = x, Breitengrad = y)
pos = {
   node: (data['lon'], data['lat']) for node, data in graph.nodes(data=True)
}
# Plot starten
plt.figure(figsize=(10, 8))
# Knoten und Kanten zeichnen
nx.draw(
   graph,
   pos,
   with_labels=True,
   node_size=600,
   node_color='lightblue',
   edge_color='gray',
   font_size=8
)
# Kantengewichte (Distanz in Metern) beschriften
edge_labels = nx.get_edge_attributes(graph, 'weight')
formatted_labels = {edge: f"{dist:.0f} m" for edge, dist in edge_labels.items()}
nx.draw_networkx_edge_labels(graph, pos, edge_labels=formatted_labels, font_size=7)
# Plot beschriften
plt.title(f"Graph mit Distanzlimit {MAX_DISTANZ} m")
plt.xlabel("Längengrad")
plt.ylabel("Breitengrad")
plt.axis("equal")
plt.grid(True)
plt.tight_layout()
plt.show()