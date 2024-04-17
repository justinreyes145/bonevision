# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patientTableVELbWv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.13
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_PatientQ(object):
    def setupUi(self, PatientQ):
        if not PatientQ.objectName():
            PatientQ.setObjectName(u"PatientQ")
        PatientQ.resize(1123, 526)
        self.PIButtons = QDialogButtonBox(PatientQ)
        self.PIButtons.setObjectName(u"PIButtons")
        self.PIButtons.setGeometry(QRect(460, 490, 171, 32))
        self.PIButtons.setOrientation(Qt.Horizontal)
        self.PIButtons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.PatientInfo = QTableWidget(PatientQ)
        if (self.PatientInfo.columnCount() < 6):
            self.PatientInfo.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.PatientInfo.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.PatientInfo.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.PatientInfo.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.PatientInfo.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.PatientInfo.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.PatientInfo.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.PatientInfo.setObjectName(u"PatientInfo")
        self.PatientInfo.setGeometry(QRect(23, 20, 1076, 461))
        self.PatientInfo.horizontalHeader().setMinimumSectionSize(12)
        self.PatientInfo.horizontalHeader().setDefaultSectionSize(179)

        self.retranslateUi(PatientQ)
        self.PIButtons.accepted.connect(PatientQ.accept)
        self.PIButtons.rejected.connect(PatientQ.reject)

        QMetaObject.connectSlotsByName(PatientQ)
    # setupUi

    def retranslateUi(self, PatientQ):
        PatientQ.setWindowTitle(QCoreApplication.translate("PatientQ", u"Patient Information", None))
        ___qtablewidgetitem = self.PatientInfo.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PatientQ", u"Test Number", None));
        ___qtablewidgetitem1 = self.PatientInfo.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PatientQ", u"Name ", None));
        ___qtablewidgetitem2 = self.PatientInfo.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PatientQ", u"Visit Date", None));
        ___qtablewidgetitem3 = self.PatientInfo.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PatientQ", u"Bone", None));
        ___qtablewidgetitem4 = self.PatientInfo.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PatientQ", u"Fracture?", None));
        ___qtablewidgetitem5 = self.PatientInfo.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PatientQ", u"Notes", None));
    # retranslateUi

