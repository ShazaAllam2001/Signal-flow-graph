from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class outputArea(QScrollArea):

    def __init__(self, parent=None):
        super().__init__(parent)

        # making widget resizable
        self.setWidgetResizable(True)
 
        # making qwidget object
        content = QWidget(self)
        content.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.setWidget(content)
 
        # vertical box layout
        lay = QVBoxLayout(content)
 
        # creating label
        self.label = QLabel(content)
 
        # setting font to the text
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.label.setFont(font)
        
        # styling background color
        self.label.setStyleSheet("background-color: rgb(255, 255, 255)")
        # setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
 
        # making label multi-line
        self.label.setWordWrap(True)
 
        # adding label to the layout
        lay.addWidget(self.label)


    def setText(self, text):
        # setting text to the label
        self.label.setText(text)
 
