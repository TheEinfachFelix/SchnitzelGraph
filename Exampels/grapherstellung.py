from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsLineItem
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QPen
import sys

class Node(QGraphicsEllipseItem):
    def __init__(self, x, y, radius=20):
        super().__init__(-radius, -radius, 2*radius, 2*radius)
        self.setPos(x, y)
        self.setBrush(Qt.GlobalColor.blue)
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable)
        self.edges = []  # Speichert Kanten, die mit diesem Knoten verbunden sind

class Edge(QGraphicsLineItem):
    def __init__(self, node1, node2):
        super().__init__()
        self.node1 = node1
        self.node2 = node2
        self.update_position()
        node1.edges.append(self)
        node2.edges.append(self)
        self.setPen(QPen(Qt.GlobalColor.black, 2))
    
    def update_position(self):
        self.setLine(self.node1.x(), self.node1.y(), self.node2.x(), self.node2.y())

class GraphScene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.nodes = []
        self.edges = []
        self.temp_selected_nodes = []

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:  # Linksklick -> Knoten hinzufügen
            node = Node(event.scenePos().x(), event.scenePos().y())
            self.addItem(node)
            self.nodes.append(node)
        elif event.button() == Qt.MouseButton.RightButton:  # Rechtsklick -> Kante erstellen
            items = self.items(event.scenePos())
            clicked_nodes = [item for item in items if isinstance(item, Node)]
            if clicked_nodes:
                self.temp_selected_nodes.append(clicked_nodes[0])
                if len(self.temp_selected_nodes) == 2:
                    node1, node2 = self.temp_selected_nodes
                    edge = Edge(node1, node2)
                    self.addItem(edge)
                    self.edges.append(edge)
                    self.temp_selected_nodes = []
        super().mousePressEvent(event)

class GraphView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = GraphScene()
        self.setScene(self.scene)
        #self.setRenderHint(QGraphicsView.RenderHint.Antialiasing)
    
    def get_graph_data(self):
        data = {
            "nodes": [(node.x(), node.y()) for node in self.scene.nodes],
            "edges": [((edge.node1.x(), edge.node1.y()), (edge.node2.x(), edge.node2.y())) for edge in self.scene.edges]
        }
        return data

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = GraphView()
    view.show()
    app.exec()