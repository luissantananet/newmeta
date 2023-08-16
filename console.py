# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader




def showdados():
    dados.show()


if __name__ == "__main__":
    app = QApplication([])
    ui_file_name = (r'.\frms\main.ui')
    ui_frmdados = (r'.\frms\atualizardados.ui')
    ui_main = QFile(ui_file_name)
    ui_frmdados = QFile(r'.\frms\atualizardados.ui')
    loader = QUiLoader()
    window = loader.load(ui_main)
    dados = loader.load(ui_frmdados)
    # Botões From main
    window.actionImportar_Dados.triggered.connect(showdados)
    window.show()
    sys.exit(app.exec())
    