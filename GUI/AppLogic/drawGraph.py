from PyQt5.QtWidgets import *

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import networkx as nx
from copy import deepcopy 

class Graph():

    def __init__(self, scene: QGraphicsScene):
        self.scene = scene
        self.graph = nx.DiGraph()
        self.undoList = []
        self.redoList = []

    def refresh_figure(self):
        self.figure = Figure()
        self.axes = self.figure.gca()
        pos = nx.planar_layout(self.graph)
        nx.draw(self.graph, pos, self.axes, with_labels=True)
        labels = nx.get_edge_attributes(self.graph,'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, ax=self.axes, edge_labels=labels)

        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(720,610)
        self.scene.addWidget(self.canvas)

    def add_node(self, node: str):
        self.undoList.append(deepcopy(self.graph))
        self.graph.add_node(node)
        self.refresh_figure()

    def add_edge(self, fromNode: str, toNode: str, weight: str):
        self.undoList.append(deepcopy(self.graph))
        self.graph.add_edge(fromNode, toNode, weight=weight)
        self.refresh_figure()

    def undo(self):
        if len(self.undoList) > 0:
            self.redoList.append(self.graph)
            self.graph = self.undoList.pop()
            self.refresh_figure()

    def redo(self):
        if len(self.redoList) > 0:
            self.graph = self.redoList.pop()
            self.undoList.append(self.graph)
            self.refresh_figure()