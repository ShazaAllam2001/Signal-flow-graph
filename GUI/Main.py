from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from drawArea import drawArea
from outputArea import outputArea
from AppLogic.drawGraph import graph


class Ui_MainWindow(QMainWindow):
    G = graph()

    def __init__(self, parent=None):
        super().__init__(parent)

        """ intializting window attributes """

        self.setWindowTitle(u"Signal flow graph Simulator")
        self.resize(1200, 650)

        icon = QIcon()
        icon.addFile(u"Icons/nodes-60px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.setStyleSheet(u"background-color: rgb(238, 238, 238);")

        """ adding window components """
        self.Ui_Components()
        

    def Ui_Components(self):
        """ window components """

        self.tool_bar()

        # Drawing Area
        self.drawArea = QGraphicsView(self)
        self.drawArea.setObjectName(u"drawArea")
        self.drawArea.setGeometry(QRect(20, 60, 720, 570))
        self.drawScene = drawArea(self.drawArea)
        self.drawArea.setScene(self.drawScene)
        self.drawArea.setSceneRect(0, 0, 720, 610)
        
        self.output_box()

    def tool_bar(self):
        # toolBar
        self.toolBar = QGroupBox(self)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setGeometry(QRect(20, 20, 720, 40))
        self.toolBar.setStyleSheet(u"border: none;")

        # Node name line edit
        """ for writing the name of the node to be added """
        self.nodeName = QLineEdit(self.toolBar)
        self.nodeName.setObjectName(u"nodeName")
        self.nodeName.setGeometry(QRect(0, 0, 140, 30))
        font1 = QFont()
        font1.setPointSize(11)
        self.nodeName.setFont(font1)
        self.nodeName.setStyleSheet(u"QLineEdit#nodeName {\n"
                                     "border : 1px solid black;\n"
                                     "background-color: white;\n"
                                     "color: rgb(63,63,63);\n"
                                     "}\n"
                                     "QLineEdit#nodeName:focus {\n"
                                     "border-color : blue; \n"
                                     "}")

        # Add node button
        """ for adding a node to the graph """
        self.add = QPushButton(self.toolBar)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(150, 0, 140, 30))
        self.add.setMouseTracking(True)
        self.add.setStyleSheet(u"QPushButton#add {\n"
                                 "border : 3px solid rgb(200, 0, 0);\n"
                                 "background-color: rgb(200, 0, 0);\n"
                                 "color: white;\n"
                                 "}\n"
                                 "QPushButton#add:hover {\n"
                                 "border-color : white; \n"
                                 "}")
        font2 = QFont()
        font2.setFamily(u"Serif")
        font2.setPointSize(13)
        self.add.setFont(font2)
        self.add.setText(u"Add Node")
        self.add.clicked.connect(lambda: graph.add_node('fooData'))
        
    def output_box(self):
        # Output box
        self.output = QGroupBox(self)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(760, 20, 420, 610))
        font3 = QFont()
        font3.setFamily(u"Calisto MT")
        font3.setPointSize(16)
        font3.setItalic(True)
        self.output.setFont(font3)
        self.output.setStyleSheet(u"color: rgb(150, 0, 0);")
        self.output.setTitle(u"Output")

        # Forward paths label
        self.forwardPathLabel = QLabel(self.output)
        self.forwardPathLabel.setObjectName(u"forwardPathLabel")
        self.forwardPathLabel.setGeometry(QRect(15, 30, 200, 20))
        font4 = QFont()
        font4.setFamily(u"Lucida Sans Unicode")
        font4.setPointSize(11)
        self.forwardPathLabel.setFont(font4)
        self.forwardPathLabel.setStyleSheet(u"color: black;")
        self.forwardPathLabel.setText(u"Forward paths = ")

        # Forward path
        """ for displaying Forward paths """
        self.forwardPath = outputArea(self.output)
        self.forwardPath.setObjectName(u"forwardPath")
        self.forwardPath.setGeometry(QRect(15, 55, 390, 100))

        # Loops label
        self.loopsLabel = QLabel(self.output)
        self.loopsLabel.setObjectName(u"loopsLabel")
        self.loopsLabel.setGeometry(QRect(15, 160, 200, 20))
        self.loopsLabel.setFont(font4)
        self.loopsLabel.setStyleSheet(u"color: black;")
        self.loopsLabel.setText(u"Loops = ")

        # Loops
        """ for displaying Loops """
        self.loops = outputArea(self.output)
        self.loops.setObjectName(u"loops")
        self.loops.setGeometry(QRect(15, 185, 390, 100))

        # Non-touchings Loops label
        self.nonTouchingLabel = QLabel(self.output)
        self.nonTouchingLabel.setObjectName(u"nonTouchingLabel")
        self.nonTouchingLabel.setGeometry(QRect(15, 290, 200, 20))
        self.nonTouchingLabel.setFont(font4)
        self.nonTouchingLabel.setStyleSheet(u"color: black;")
        self.nonTouchingLabel.setText(u"Non-touching Loops = ")

        # Non-touching Loops
        """ for displaying Non-touching Loops """
        self.nonTouching = outputArea(self.output)
        self.nonTouching.setObjectName(u"nonTouching")
        self.nonTouching.setGeometry(QRect(15, 315, 390, 100))

        # Transfer function label
        self.transferLabel = QLabel(self.output)
        self.transferLabel.setObjectName(u"transferLabel")
        self.transferLabel.setGeometry(QRect(15, 420, 200, 20))
        self.transferLabel.setFont(font4)
        self.transferLabel.setStyleSheet(u"color: black;")
        self.transferLabel.setText(u"Transfer function = ")

        # Transfer function
        """ for displaying Non-touching Loops """
        self.transfer = outputArea(self.output)
        self.transfer.setObjectName(u"transfer")
        self.transfer.setGeometry(QRect(15, 445, 390, 100))

        # Solve button
        """ for sloving the graph """
        self.solve = QPushButton(self.output)
        self.solve.setObjectName(u"solve")
        self.solve.setGeometry(QRect(150, 560, 140, 40))
        self.solve.setMouseTracking(True)
        self.solve.setStyleSheet(u"QPushButton#solve {\n"
                                 "border : 4px solid rgb(46,204,113);\n"
                                 "background-color: rgb(46,204,113);\n"
                                 "color: white;\n"
                                 "}\n"
                                 "QPushButton#solve:hover {\n"
                                 "border-color : white; \n"
                                 "}")
        font5 = QFont()
        font5.setFamily(u"Calisto MT")
        font5.setPointSize(17)
        self.solve.setFont(font5)
        self.solve.setText(u"Solve")
        self.solve.clicked.connect(self.solve_clicked)


    def solve_clicked(self):
        pass



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window1 = Ui_MainWindow()
    window1.show()
    sys.exit(App.exec_())
      
     