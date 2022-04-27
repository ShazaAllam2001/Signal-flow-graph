from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from drawArea import drawArea
from outputArea import outputArea
from AppLogic.drawGraph import Graph
from solveWindow import SolveWindow


class Ui_MainWindow(QMainWindow):
    G: Graph
    solveWindow: SolveWindow

    def __init__(self, parent=None):
        super().__init__(parent)

        """ intializting window attributes """
        self.setWindowTitle(u"Signal flow graph Simulator")
        self.resize(1200, 680)

        icon = QIcon()
        icon.addFile(u"Icons/nodes-60px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.setStyleSheet(u"background-color: rgb(238, 238, 238);")

        """ adding window components """
        self.Ui_Components()
        

    def Ui_Components(self):
        """ window components """
        self.tool_bar()
        self.output_box()

        # Drawing Area
        self.drawArea = QGraphicsView(self)
        self.drawArea.setObjectName(u"drawArea")
        self.drawArea.setGeometry(QRect(20, 60, 720, 600))
        self.drawScene = drawArea(self.drawArea)
        self.drawArea.setScene(self.drawScene)
        self.drawArea.setSceneRect(0, 0, 720, 600)

        self.G = Graph(self.drawScene, self.toolBar)
        self.solveWindow = SolveWindow(self.output)
    

    def tool_bar(self):
        # toolBar
        self.toolBar = QGroupBox(self)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setGeometry(QRect(20, 20, 720, 40))
        self.toolBar.setStyleSheet(u"border: none;")

        # Node name line edit
        """ for writing the name of the node to be added """
        self.nodeName = self.line_edit(QRect(0, 0, 100, 30))

        # Add node button
        self.addNode = self.add_button(QRect(105, 0, 90, 30))
        self.addNode.setText(u"Add Node")
        self.addNode.clicked.connect(lambda: self.G.add_node(self.nodeName.text()))

        # form node name line edit
        """ for writing the name of the node to be the start of the edge """
        self.fromName = self.line_edit(QRect(205, 0, 100, 30))
        self.fromName.setPlaceholderText(u"From")

        # to node name line edit
        """ for writing the name of the node to be the end of the edge """
        self.toName = self.line_edit(QRect(310, 0, 100, 30))
        self.toName.setPlaceholderText(u"To")

        # edge weight line edit
        """ for writing the weight of the edge """
        self.weight = self.line_edit(QRect(415, 0, 100, 30))
        self.weight.setPlaceholderText(u"Weight")

        # Add edge button
        self.addEdge = self.add_button(QRect(520, 0, 90, 30))
        self.addEdge.setText(u"Add Edge")
        self.addEdge.clicked.connect(lambda: self.G.add_edge(self.fromName.text(), self.toName.text(), self.weight.text()))
        
        # Undo button
        self.undo = self.undo_redo(QRect(620, 0, 45, 30))
        self.undo.setToolTip(u"Undo")
        icon1 = QIcon()
        icon1.addFile(u"Icons/icons8-undo-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.undo.setIcon(icon1)
        self.undo.setIconSize(QSize(24, 24))
        self.undo.clicked.connect(lambda: self.G.undo())

        # Redo button
        self.redo = self.undo_redo(QRect(675, 0, 45, 30))
        self.redo.setToolTip(u"Redo")
        icon2 = QIcon()
        icon2.addFile(u"Icons/icons8-redo-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.redo.setIcon(icon2)
        self.redo.setIconSize(QSize(24, 24))
        self.redo.clicked.connect(lambda: self.G.redo())
        
    def line_edit(self, geometry: QRect):
        lineEdit = QLineEdit(self.toolBar)
        lineEdit.setObjectName(u"nodeName")
        lineEdit.setGeometry(geometry)
        font1 = QFont()
        font1.setPointSize(11)
        lineEdit.setFont(font1)
        lineEdit.setStyleSheet(u"QLineEdit#nodeName {\n"
                                     "border : 1px solid black;\n"
                                     "background-color: white;\n"
                                     "color: rgb(63,63,63);\n"
                                     "padding-left: 5px;\n"
                                     "}\n"
                                     "QLineEdit#nodeName:focus {\n"
                                     "border-color : blue; \n"
                                     "}")
        return lineEdit

    def add_button(self, geometry: QRect):
        addButton = QPushButton(self.toolBar)
        addButton.setObjectName(u"add")
        addButton.setGeometry(geometry)
        addButton.setMouseTracking(True)
        addButton.setStyleSheet(u"QPushButton#add {\n"
                                 "border : 3px solid rgb(200, 0, 0);\n"
                                 "background-color: rgb(200, 0, 0);\n"
                                 "color: white;\n"
                                 "}\n"
                                 "QPushButton#add:hover {\n"
                                 "border-color : white; \n"
                                 "}")
        font2 = QFont()
        font2.setFamily(u"Serif")
        font2.setPointSize(11)
        addButton.setFont(font2)
        return addButton

    def undo_redo(self, geometry: QRect):
        undoRedo = QPushButton(self.toolBar)
        undoRedo.setObjectName(u"undoRedo")
        undoRedo.setGeometry(geometry)
        undoRedo.setMouseTracking(True)
        undoRedo.setStyleSheet(u"QPushButton#undoRedo {\n"
                                 "border-radius : 5;\n"
                                 "border : 2px solid black;\n"
                                 "}\n"
                                 "QPushButton#undoRedo:hover {\n"
                                 "background-color : rgb(225, 225, 225);\n"
                                 "}")
        return undoRedo

    def output_box(self):
        # Output box
        self.output = QGroupBox(self)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(760, 20, 420, 640))
        font3 = QFont()
        font3.setFamily(u"Calisto MT")
        font3.setPointSize(17)
        font3.setItalic(True)
        self.output.setFont(font3)
        self.output.setStyleSheet(u"color: rgb(150, 0, 0);")
        self.output.setTitle(u"Output")

        # Forward paths label
        self.forwardPathLabel = self.label(QRect(15, 30, 200, 20))
        self.forwardPathLabel.setText(u"Forward paths = ")

        # Forward path
        """ for displaying Forward paths """
        self.forwardPath = outputArea(self.output)
        self.forwardPath.setObjectName(u"forwardPath")
        self.forwardPath.setGeometry(QRect(15, 55, 390, 90))
        self.forwardPath.setStyleSheet(u"color: rgb(88, 92, 122);")

        # Loops label
        self.loopsLabel = self.label(QRect(15, 150, 200, 20))
        self.loopsLabel.setText(u"Loops = ")

        # Loops
        """ for displaying Loops """
        self.loops = outputArea(self.output)
        self.loops.setObjectName(u"loops")
        self.loops.setGeometry(QRect(15, 175, 390, 90))
        self.loops.setStyleSheet(u"color: rgb(88, 92, 122);")

        # Non-touchings Loops label
        self.nonTouchingLabel = self.label(QRect(15, 270, 200, 20))
        self.nonTouchingLabel.setText(u"Non-touching Loops = ")

        # Non-touching Loops
        """ for displaying Non-touching Loops """
        self.nonTouching = outputArea(self.output)
        self.nonTouching.setObjectName(u"nonTouching")
        self.nonTouching.setGeometry(QRect(15, 295, 390, 90))
        self.nonTouching.setStyleSheet(u"color: rgb(88, 92, 122);")

        # Delta label
        self.nonTouchingLabel = self.label(QRect(15, 390, 200, 20))
        self.nonTouchingLabel.setText(u"Deltas = ")

        # Deltas
        """ for displaying Delta values """
        self.nonTouching = outputArea(self.output)
        self.nonTouching.setObjectName(u"delta")
        self.nonTouching.setGeometry(QRect(15, 415, 390, 90))
        self.nonTouching.setStyleSheet(u"color: rgb(88, 92, 122);")

        # Transfer function label
        self.transferLabel = self.label(QRect(15, 510, 200, 20))
        self.transferLabel.setText(u"Transfer function = ")

        # Transfer function
        """ for displaying Non-touching Loops """
        self.transfer = outputArea(self.output)
        self.transfer.setObjectName(u"transfer")
        self.transfer.setGeometry(QRect(15, 535, 390, 45))
        self.transfer.setStyleSheet(u"color: rgb(88, 92, 122);")

        # Solve button
        """ for sloving the graph """
        self.solve = QPushButton(self.output)
        self.solve.setObjectName(u"solve")
        self.solve.setGeometry(QRect(140, 590, 140, 40))
        self.solve.setMouseTracking(True)
        self.solve.setStyleSheet(u"QPushButton#solve {\n"
                                 "border : 4px solid rgb(46,204,113);\n"
                                 "background-color: rgb(46,204,113);\n"
                                 "color: white;\n"
                                 "}\n"
                                 "QPushButton#solve:hover {\n"
                                 "border-color : white; \n"
                                 "}")
        self.solve.setFont(font3)
        self.solve.setText(u"Solve")
        self.solve.clicked.connect(lambda: self.solveWindow.show(self.G.graph))

    def label(self, geometry: QRect):
        label = QLabel(self.output)
        label.setObjectName(u"label")
        label.setGeometry(geometry)
        font4 = QFont()
        font4.setFamily(u"Lucida Sans Unicode")
        font4.setPointSize(11)
        label.setFont(font4)
        label.setStyleSheet(u"color: black;")
        return label



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(App.exec_())
          
