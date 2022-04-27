from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import networkx as nx

from AppLogic.solveGraph import SolveGraph

class SolveWindow(QWidget):
    solve: SolveGraph

    def __init__(self, output: QGroupBox, parent=None):
        super().__init__(parent)
        self.solve = SolveGraph(output)

        """ intializting window attributes """
        self.setWindowTitle(u"Give Input & Output")
        self.resize(280, 170)

        icon = QIcon()
        icon.addFile(u"Icons/nodes-60px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.setStyleSheet(u"background-color: rgb(238, 238, 238);")

        """ adding window components """
        self.Ui_Components()

    def Ui_Components(self):

        # source label 
        self.sourceLabel = QLabel(self)
        self.sourceLabel.setObjectName(u"sourceLabel")
        self.sourceLabel.setGeometry(QRect(20, 20, 100, 23))
        font = QFont()
        font.setPointSize(11)
        self.sourceLabel.setFont(font)
        self.sourceLabel.setText(u"Input (Source)")

        # target label 
        self.targetLabel = QLabel(self)
        self.targetLabel.setObjectName(u"targetLabel")
        self.targetLabel.setGeometry(QRect(20, 70, 100, 23))
        self.targetLabel.setFont(font)
        self.targetLabel.setText(u"Output (target)")
        

        """ Score Value """
        self.source = QLineEdit(self)
        self.source.setObjectName(u"source")
        self.source.setGeometry(QRect(130, 20, 130, 27))
        self.source.setFont(font)
        self.source.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.source.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                  "border: 1px solid black;\n"
                                  "color: rgb(88, 92, 122);")

        """ Target Value """
        self.target = QLineEdit(self)
        self.target.setObjectName(u"target")
        self.target.setGeometry(QRect(130, 70, 130, 27))
        self.target.setFont(font)
        self.target.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.target.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                  "border: 1px solid black;\n"
                                  "color: rgb(88, 92, 122);")

        # Solve button
        """ for sloving the graph """
        self.solveBtn = QPushButton(self)
        self.solveBtn.setObjectName(u"solveBtn")
        self.solveBtn.setGeometry(QRect(100, 120, 100, 30))
        self.solveBtn.setMouseTracking(True)
        self.solveBtn.setStyleSheet(u"QPushButton#solveBtn {\n"
                                 "border : 3px solid black;\n"
                                 "background-color: black;\n"
                                 "color: white;\n"
                                 "}\n"
                                 "QPushButton#solveBtn:hover {\n"
                                 "border-color : white; \n"
                                 "}")
        self.solveBtn.setFont(font)
        self.solveBtn.setText(u"Solve")
        self.solveBtn.clicked.connect(lambda: self.hide())

    def show(self, graph: nx.DiGraph):
        self.solve.graph = graph
        super().show()

    def hide(self):
        self.solve.solve(self.source.text(), self.target.text())
        super().hide()
        self.source.setText("")
        self.target.setText("")
        