from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from pymongo import MongoClient
import os

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Bonevision"]
collection = db["user_info"]

class Ui_HistorySearchPage(object):
    def setupUi(self, HistorySearchPage):
        if not HistorySearchPage.objectName():
            HistorySearchPage.setObjectName(u"HistorySearchPage")
        HistorySearchPage.resize(800, 600)
        self.centralwidget = QWidget(HistorySearchPage)
        self.centralwidget.setObjectName(u"centralwidget")

        # Search input
        self.searchLabel = QLabel(self.centralwidget)
        self.searchLabel.setObjectName(u"searchLabel")
        self.searchLabel.setGeometry(QRect(50, 50, 150, 30))
        self.searchLabel.setText("Enter Name:")

        self.searchLineEdit = QLineEdit(self.centralwidget)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setGeometry(QRect(150, 50, 200, 30))

        self.searchButton = QPushButton(self.centralwidget)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(380, 50, 100, 30))
        self.searchButton.setText("Search")
        self.searchButton.clicked.connect(self.searchHistory)

        # Results display
        self.resultsLabel = QLabel(self.centralwidget)
        self.resultsLabel.setObjectName(u"resultsLabel")
        self.resultsLabel.setGeometry(QRect(50, 100, 200, 30))
        self.resultsLabel.setText("Search Results:")

        self.resultsListWidget = QListWidget(self.centralwidget)
        self.resultsListWidget.setObjectName(u"resultsListWidget")
        self.resultsListWidget.setGeometry(QRect(50, 140, 700, 300))

        self.resultsListWidget.itemDoubleClicked.connect(self.showDetails)

        # Image display
        self.imageLabel = QLabel(self.centralwidget)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setGeometry(QRect(50, 460, 700, 100))

        HistorySearchPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(HistorySearchPage)
        QMetaObject.connectSlotsByName(HistorySearchPage)

    def retranslateUi(self, HistorySearchPage):
        HistorySearchPage.setWindowTitle(QCoreApplication.translate("HistorySearchPage", u"History Search Page", None))
        self.searchLabel.setText(QCoreApplication.translate("HistorySearchPage", u"Enter Name:", None))
        self.searchButton.setText(QCoreApplication.translate("HistorySearchPage", u"Search", None))
        self.resultsLabel.setText(QCoreApplication.translate("HistorySearchPage", u"Search Results:", None))

    def searchHistory(self):
        name = self.searchLineEdit.text().strip()
        if name:
            # Clear previous search results
            self.resultsListWidget.clear()

            # Query the database for matching entries
            matching_entries = collection.find({"name": name})

            # Display results in the list widget
            for entry in matching_entries:
                visit_date = entry.get("date_of_visit", "")
                birth_date = entry.get("date_of_birth", "")
                result = entry.get("additional_notes", "")
                item_text = f"Visit Date: {visit_date}, Birth Date: {birth_date}, Result: {result}"
                self.resultsListWidget.addItem(item_text)

    def showDetails(self, item):
        # Get the selected item text
        selected_text = item.text()

        # Extract visit date, birth date, and result from the selected text
        visit_date = selected_text.split(",")[0].split(":")[1].strip()
        birth_date = selected_text.split(",")[1].split(":")[1].strip()
        result = selected_text.split(",")[2].split(":")[1].strip()

        # Display details in a message box
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle("Details")
        msgBox.setText(f"Visit Date: {visit_date}\nBirth Date: {birth_date}\nResult: {result}")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
