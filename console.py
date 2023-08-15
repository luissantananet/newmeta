# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from frms.ui_main import Ui_MainWindow


class principal(QMainWindow):
    def __init__(self):
        super(principal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    #ui_file = QUiLoader.load(r'.\frms\main.ui')
    window = principal()
    window.show()
    sys.exit(app.exec())
