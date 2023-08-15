# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow


class principal(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


if __name__ == "__main__":
    app = QApplication([])
    window = principal()
    window.show()
    sys.exit(app.exec())
