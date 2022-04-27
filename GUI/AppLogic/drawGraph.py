from PyQt5.QtWidgets import *

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import networkx as nx
from copy import deepcopy  

from AppLogic.errorMessage import ErrorMessage

class Graph():

    def __init__(self, scene: QGraphicsScene, toolBar: QGroupBox):
        self.scene = scene
        self.toolBar = toolBar.children()
        self.graph = nx.DiGraph()
        self.undoList = []
        self.redoList = []

    def refresh_figure(self):
        self.figure = Figure()
        self.axes = self.figure.gca()
        pos = nx.planar_layout(self.graph)
        nx.draw(self.graph, pos, self.axes, with_labels=True)
        labels = nx.get_edge_attributes(self.graph,'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, ax=self.axes, edge_labels=labels, clip_on=False)

        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(720,610)
        self.scene.addWidget(self.canvas)

    def add_node(self, node: str):
        self.undoList.append(deepcopy(self.graph))
        self.redoList = []
        if node == "":
            message = ErrorMessage("Node name did not entered!")
            message.show()
        else:
            self.graph.add_node(node)
            self.refresh_figure()
        self.toolBar[0].setText("")

    def add_edge(self, fromNode: str, toNode: str, weight: str):
        self.undoList.append(deepcopy(self.graph))
        self.redoList = []
        if fromNode == "" or toNode == "" or weight == "":
            message = ErrorMessage("Edge information did not entered!")
            message.show()
        else:
            if self.graph.has_node(fromNode) and self.graph.has_node(toNode):
                self.graph.add_edge(fromNode, toNode, weight=weight)
                self.refresh_figure()
            else:
                message = ErrorMessage("Nodes does not exist in graph!")
                message.show()
        self.toolBar[2].setText("")
        self.toolBar[3].setText("")
        self.toolBar[4].setText("")

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
