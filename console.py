# This Python file uses the following encoding: utf-8
import sys
import sqlite3
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
# Criando Bando de dados
banco = sqlite3.connect(r'.\dados\dados.db')
cursor = banco.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS dasdos(
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               dep varchar(100), 
               cat varchar(100), 
               subcat varchar(100),
               compra decimal(10,2),
               venda decimal(10,2),
               markup decimal(5,2),
               custo_saida decimal(10,2),
               valormargem_lucro decimal(10,2),
               deferencavalor decimal(10,2)
               )""")



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
    