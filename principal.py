# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import uic

class principal(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


if __name__ == "__main__":
    app = QApplication([])
    frm_inicial = uic.loadUi(r'.\frms\main.ui')
    #window = principal()
    frm_inicial.show()
    sys.exit(app.exec())
