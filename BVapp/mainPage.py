# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainPagetTIAZS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.12
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

#import mainDialogBox_rc

class Ui_mainPage(object):
    def saveStringInfo(self):
        patientName = self.nameField.toPlainText() #Use this as a template for the rest of the fields
        filename = "%s.txt" % patientName
        with open(filename,'w') as patientProfile:
            patientProfile.write(patientName) #We are gonna write the information like this

    def setupUi(self, mainPage):
        if not mainPage.objectName():
            mainPage.setObjectName(u"mainPage")
        mainPage.resize(1100, 600)
        self.actionNew = QAction(mainPage)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(mainPage)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(mainPage)
        self.actionClose.setObjectName(u"actionClose")
        self.centralwidget = QWidget(mainPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.outputPane = QTextBrowser(self.centralwidget)
        self.outputPane.setObjectName(u"outputPane")
        self.outputPane.setGeometry(QRect(325, 10, 291, 471))
        self.imagePane = QLabel(self.centralwidget)
        self.imagePane.setObjectName(u"imagePane")
        self.imagePane.setGeometry(QRect(650, 10, 381, 475))
        self.imagePane.setPixmap(QPixmap("IMG0000019-1.jpg"))
        self.printButton = QPushButton(self.centralwidget)
        self.printButton.setObjectName(u"printButton")
        self.printButton.setGeometry(QRect(900, 510, 121, 27))
        self.uploadButton = QPushButton(self.centralwidget)
        self.uploadButton.setObjectName(u"uploadButton")
        self.uploadButton.setGeometry(QRect(775, 510, 121, 27))
        self.showFullImageButton = QPushButton(self.centralwidget)
        self.showFullImageButton.setObjectName(u"showFullImageButton")
        self.showFullImageButton.setGeometry(QRect(650, 510, 121, 27))
        self.nameField = QTextEdit(self.centralwidget)
        self.nameField.setObjectName(u"nameField")
        self.nameField.setGeometry(QRect(10, 50, 291, 31))
        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(10, 20, 100, 19))
        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setGeometry(QRect(10, 90, 100, 19))
        self.bdateLabel = QLabel(self.centralwidget)
        self.bdateLabel.setObjectName(u"bdateLabel")
        self.bdateLabel.setGeometry(QRect(10, 150, 100, 19))
        self.dateMonth = QTextEdit(self.centralwidget)
        self.dateMonth.setObjectName(u"dateMonth")
        self.dateMonth.setGeometry(QRect(10, 110, 30, 30))
        self.dateDay = QTextEdit(self.centralwidget)
        self.dateDay.setObjectName(u"dateDay")
        self.dateDay.setGeometry(QRect(55, 110, 30, 30))
        self.dateYear = QTextEdit(self.centralwidget)
        self.dateYear.setObjectName(u"dateYear")
        self.dateYear.setGeometry(QRect(100, 110, 60, 30))
        self.bdateMonth = QTextEdit(self.centralwidget)
        self.bdateMonth.setObjectName(u"bdateMonth")
        self.bdateMonth.setGeometry(QRect(10, 170, 30, 30))
        self.bdateDay = QTextEdit(self.centralwidget)
        self.bdateDay.setObjectName(u"bdateDay")
        self.bdateDay.setGeometry(QRect(55, 170, 30, 30))
        self.bdateYear = QTextEdit(self.centralwidget)
        self.bdateYear.setObjectName(u"bdateYear")
        self.bdateYear.setGeometry(QRect(100, 170, 60, 30))
        self.dateDash1 = QLabel(self.centralwidget)
        self.dateDash1.setObjectName(u"dateDash1")
        self.dateDash1.setGeometry(QRect(45, 115, 12, 19))
        self.dateDash2 = QLabel(self.centralwidget)
        self.dateDash2.setObjectName(u"dateDash2")
        self.dateDash2.setGeometry(QRect(90, 115, 15, 19))
        self.bdateDash1 = QLabel(self.centralwidget)
        self.bdateDash1.setObjectName(u"bdateDash1")
        self.bdateDash1.setGeometry(QRect(45, 175, 12, 19))
        self.bdateDash2 = QLabel(self.centralwidget)
        self.bdateDash2.setObjectName(u"bdateDash2")
        self.bdateDash2.setGeometry(QRect(90, 175, 12, 19))
        self.contextPane = QTextEdit(self.centralwidget)
        self.contextPane.setObjectName(u"contextPane")
        self.contextPane.setGeometry(QRect(10, 240, 300, 241))
        self.notesLabel = QLabel(self.centralwidget)
        self.notesLabel.setObjectName(u"notesLabel")
        self.notesLabel.setGeometry(QRect(10, 210, 150, 19))
        self.saveInfo = QPushButton(self.centralwidget)
        self.saveInfo.setObjectName(u"saveInfo")
        self.saveInfo.setGeometry(QRect(60, 510, 200, 27))
        self.saveInfo.clicked.connect(self.saveStringInfo)
        mainPage.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainPage)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1100, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuEdit.setGeometry(QRect(454, 458, 157, 54))
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        mainPage.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainPage)
        self.statusbar.setObjectName(u"statusbar")
        mainPage.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)

        self.retranslateUi(mainPage)

        QMetaObject.connectSlotsByName(mainPage)
    # setupUi

    def retranslateUi(self, mainPage):
        mainPage.setWindowTitle(QCoreApplication.translate("mainPage", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("mainPage", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("mainPage", u"Open", None))
        self.actionClose.setText(QCoreApplication.translate("mainPage", u"Close", None))
        self.outputPane.setHtml(QCoreApplication.translate("mainPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                       "p, li { white-space: pre-wrap; }\n"
                                                                       "</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Output Text</p>\n"
                                                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Goes Here</p>\n"
                                                                       "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.imagePane.setText("")
        self.printButton.setText(QCoreApplication.translate("mainPage", u"Print", None))
        self.uploadButton.setText(QCoreApplication.translate("mainPage", u"Upload", None))
        self.showFullImageButton.setText(QCoreApplication.translate("mainPage", u"Show Full Image", None))
        self.nameField.setHtml(QCoreApplication.translate("mainPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                      "p, li { white-space: pre-wrap; }\n"
                                                                      "</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                                      "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">John Smith</p>\n"
                                                                      "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.nameLabel.setText(QCoreApplication.translate("mainPage", u"Name: ", None))
        self.dateLabel.setText(QCoreApplication.translate("mainPage", u"Date of Visit: ", None))
        self.bdateLabel.setText(QCoreApplication.translate("mainPage", u"Date of Birth", None))
        self.dateMonth.setHtml(QCoreApplication.translate("mainPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                      "p, li { white-space: pre-wrap; }\n"
                                                                      "</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                                      "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12</p></body></html>", None))
        self.dateDay.setHtml(QCoreApplication.translate("mainPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                    "p, li { white-space: pre-wrap; }\n"
                                                                    "</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12</p></body></html>", None))
        self.dateYear.setHtml(QCoreApplication.translate("mainPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                     "p, li { white-space: pre-wrap; }\n"
                                                                     "</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12</p></body></html>", None))
        self.dateDash1.setText(QCoreApplication.translate("mainPage", u"/", None))
        self.dateDash2.setText(QCoreApplication.translate("mainPage", u"/", None))
        self.bdateDash1.setText(QCoreApplication.translate("mainPage", u"/", None))
        self.bdateDash2.setText(QCoreApplication.translate("mainPage", u"/", None))
        self.notesLabel.setText(QCoreApplication.translate("mainPage", u"Additional Notes: ", None))
        self.saveInfo.setText(QCoreApplication.translate("mainPage", u"Save Patient Information", None))
        self.menuFile.setTitle(QCoreApplication.translate("mainPage", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("mainPage", u"Edit", None))
        self.menuAbout.setTitle(QCoreApplication.translate("mainPage", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("mainPage", u"Help", None))
    # retranslateUi
