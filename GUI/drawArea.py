from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class drawArea(QGraphicsScene):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setBackgroundBrush(QColor("#FFFFFF"))

