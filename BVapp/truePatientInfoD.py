from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from pymongo import MongoClient
from mainPage import Ui_mainPage

class Ui_Dialog(object):
    def setupUi1(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 287)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 230, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 50, 340, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 130, 340, 16))
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 70, 341, 41))
        self.textEdit_2 = QTextEdit(Dialog)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(30, 160, 341, 41))
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.check_patient_info)
        self.buttonBox.rejected.connect(Dialog.close)  # Changed from reject to close
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Patient Name", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Patient Date of Birth (MMDDYYYY)", None))

    def check_patient_info(self):
        patient_name = self.textEdit.toPlainText()
        patient_dob = self.textEdit_2.toPlainText()

        # Connect to MongoDB
        client = MongoClient("mongodb://localhost:27017/")
        db = client["Bonevision"]
        collection = db["user_info"]

        # Query the database to check if the patient information exists
        result = collection.find_one({"name": patient_name, "date_of_birth": patient_dob})
        if result:
            # Open the main page if patient information is found
            self.open_main_page()
        else:
            # Inform the user if no matching information is found
            QMessageBox.critical(None, "Error", "Patient information not found.")

    def open_main_page(self):
        self.mainPage = QMainWindow()
        self.ui_mainPage = Ui_mainPage()
        self.ui_mainPage.setupUi(self.mainPage)
        self.mainPage.show()