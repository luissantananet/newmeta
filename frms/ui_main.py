# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStackedWidget, QStatusBar,
    QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionImportar_Dados = QAction(MainWindow)
        self.actionImportar_Dados.setObjectName(u"actionImportar_Dados")
        self.actionConfiguracao = QAction(MainWindow)
        self.actionConfiguracao.setObjectName(u"actionConfiguracao")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 791, 341))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 10, 471, 24))
        self.toolButton = QToolButton(self.page)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(500, 10, 23, 23))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuDados = QMenu(self.menubar)
        self.menuDados.setObjectName(u"menuDados")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDados.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuDados.addAction(self.actionImportar_Dados)
        self.menuHelp.addAction(self.actionConfiguracao)
        self.menuHelp.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionImportar_Dados.setText(QCoreApplication.translate("MainWindow", u"Importar Dados", None))
        self.actionConfiguracao.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00e3o", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.menuDados.setTitle(QCoreApplication.translate("MainWindow", u"Dados", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

