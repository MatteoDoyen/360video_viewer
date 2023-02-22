# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1125, 591)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.haut_gauche = QPushButton(self.centralwidget)
        self.haut_gauche.setObjectName(u"haut_gauche")
        self.haut_gauche.setCheckable(True)
        self.haut_gauche.setAutoRepeat(True)

        self.verticalLayout_2.addWidget(self.haut_gauche)

        self.gauche = QPushButton(self.centralwidget)
        self.gauche.setObjectName(u"gauche")
        self.gauche.setCheckable(True)
        self.gauche.setAutoRepeat(True)

        self.verticalLayout_2.addWidget(self.gauche)

        self.bas_gauche = QPushButton(self.centralwidget)
        self.bas_gauche.setObjectName(u"bas_gauche")
        self.bas_gauche.setCheckable(True)
        self.bas_gauche.setAutoRepeat(True)

        self.verticalLayout_2.addWidget(self.bas_gauche)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.haut = QPushButton(self.centralwidget)
        self.haut.setObjectName(u"haut")
        self.haut.setCheckable(True)
        self.haut.setAutoRepeat(True)

        self.verticalLayout_3.addWidget(self.haut)

        self.label_view = QLabel(self.centralwidget)
        self.label_view.setObjectName(u"label_view")
        self.label_view.setMinimumSize(QSize(736, 368))
        self.label_view.setMaximumSize(QSize(736, 368))

        self.verticalLayout_3.addWidget(self.label_view)

        self.bas = QPushButton(self.centralwidget)
        self.bas.setObjectName(u"bas")
        self.bas.setCheckable(True)
        self.bas.setAutoRepeat(True)

        self.verticalLayout_3.addWidget(self.bas)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.haut_droit = QPushButton(self.centralwidget)
        self.haut_droit.setObjectName(u"haut_droit")
        self.haut_droit.setCheckable(True)
        self.haut_droit.setAutoRepeat(True)

        self.verticalLayout_4.addWidget(self.haut_droit)

        self.droit = QPushButton(self.centralwidget)
        self.droit.setObjectName(u"droit")
        self.droit.setCheckable(True)
        self.droit.setAutoRepeat(True)

        self.verticalLayout_4.addWidget(self.droit)

        self.bas_droit = QPushButton(self.centralwidget)
        self.bas_droit.setObjectName(u"bas_droit")
        self.bas_droit.setCheckable(True)
        self.bas_droit.setAutoRepeat(True)

        self.verticalLayout_4.addWidget(self.bas_droit)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1125, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.haut_gauche.setText(QCoreApplication.translate("MainWindow", u"Haut gauche", None))
        self.gauche.setText(QCoreApplication.translate("MainWindow", u"Gauche", None))
        self.bas_gauche.setText(QCoreApplication.translate("MainWindow", u"Bas gauche", None))
        self.haut.setText(QCoreApplication.translate("MainWindow", u"Haut", None))
        self.label_view.setText("")
        self.bas.setText(QCoreApplication.translate("MainWindow", u"Bas", None))
        self.haut_droit.setText(QCoreApplication.translate("MainWindow", u"Haut droit", None))
        self.droit.setText(QCoreApplication.translate("MainWindow", u"Droit", None))
        self.bas_droit.setText(QCoreApplication.translate("MainWindow", u"Bas droit", None))
    # retranslateUi

