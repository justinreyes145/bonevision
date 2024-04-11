# -*- coding: utf-8 -*-
from PySide6 import QtWidgets
################################################################################

## First Page of the GUI is made in this file
## This page's main goal is to boot up at the beginning, and the user has their options presented to them
## Once the main page is opened, this page should close, and once the main page is closed, the main page should
# open up again unless the application is fully quit out

################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from mainPage import Ui_mainPage
from truePatientInfoD import Ui_Dialog


class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_mainPage()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi1(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionDevs = QAction(MainWindow)
        self.actionDevs.setObjectName(u"actionDevs")
        self.actionReport_Bug = QAction(MainWindow)
        self.actionReport_Bug.setObjectName(u"actionReport_Bug")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(250, 50, 301, 45))
        font = QFont()
        font.setPointSize(45)
        self.nameLabel.setFont(font)
        self.descLabel = QLabel(self.centralwidget)
        self.descLabel.setObjectName(u"descLabel")
        self.descLabel.setGeometry(QRect(270, 110, 260, 19))
        self.iconLabel = QLabel(self.centralwidget)
        self.iconLabel.setObjectName(u"iconLabel")
        self.iconLabel.setGeometry(QRect(240, 140, 300, 271))
        self.iconLabel.setPixmap(QPixmap("Resources/noun-bone-3858505.png"))
        self.uploadButton = QPushButton(self.centralwidget)
        self.uploadButton.setObjectName(u"uploadButton")
        self.uploadButton.clicked.connect(self.openWindow1)
        self.uploadButton.setGeometry(QRect(320, 440, 150, 30))
        self.reloadButton = QPushButton(self.centralwidget)
        self.reloadButton.setObjectName(u"reloadButton")
        self.reloadButton.clicked.connect(self.openWindow)
        self.reloadButton.setGeometry(QRect(320, 490, 150, 30))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuAbout.addAction(self.actionDevs)
        self.menuHelp.addAction(self.actionReport_Bug)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionDevs.setText(QCoreApplication.translate("MainWindow", u"Devs", None))
        self.actionReport_Bug.setText(QCoreApplication.translate("MainWindow", u"Report Bug", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"BoneVision", None))
        self.descLabel.setText(QCoreApplication.translate("MainWindow", u"A Bone Fracture Detection Application", None))
        self.iconLabel.setText("")
        self.uploadButton.setText(QCoreApplication.translate("MainWindow", u"Exsiting Case", None))
        self.reloadButton.setText(QCoreApplication.translate("MainWindow", u"New Case", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi
