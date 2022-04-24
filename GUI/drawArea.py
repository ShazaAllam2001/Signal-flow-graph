from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import networkx as nx

class drawArea(QGraphicsScene):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.figure = Figure()
        self.axes = self.figure.gca()
        self.graph = nx.DiGraph()
        self.graph.add_node(1)
        nx.draw(self.graph, ax=self.axes)

        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(720,610)
        self.addWidget(self.canvas)

        self.setBackgroundBrush(QColor("#FFFFFF"))


    def mouseDoubleClickEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        print("hello")
        pos: QPointF = event.scenePos

        #self.clear()

        self.graph.add_node(2)
        print(self.graph.nodes())

        self.figure = Figure()
        self.axes = self.figure.gca()
        nx.draw(self.graph, ax=self.axes)

        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(720,610)

        return super().mouseDoubleClickEvent(event)


    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
       
        return super().mousePressEvent(event) 


    
    
