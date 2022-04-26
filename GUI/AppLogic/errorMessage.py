from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ErrorMessage(QMessageBox):

    def __init__(self, message: str, parent=None):
        super().__init__(parent)

        """ intializting window attributes """
        self.setWindowTitle(u"Error")
        self.setText(message)
        self.resize(280, 170)
        self.setIcon(QMessageBox.Critical)

    def show(self):
        super().exec_()

        