from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from pymongo import MongoClient
from mainPage import Ui_mainPage


# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Bone"]
collection = db["user_info"]


class HistorySearchPage(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("History Search Page")
        self.resize(800, 600)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self.centralwidget)
        layout.setSpacing(20)  # Set larger gap between widgets

        self.searchLayout = QHBoxLayout()
        self.searchLabel = QLabel("Enter Name:")
        self.searchLineEdit = QLineEdit()
        self.searchButton = QPushButton("Search")
        self.searchLayout.addWidget(self.searchLabel)
        self.searchLayout.addWidget(self.searchLineEdit)
        self.searchLayout.addWidget(self.searchButton)

        self.resultsTable = QTableWidget()
        self.resultsTable.setColumnCount(6)
        self.resultsTable.setHorizontalHeaderLabels(["Name", "Date of Visit", "Birth Date", "Bone", "Fracture", "Notes"])
        self.resultsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.resultsTable.horizontalHeader().setStretchLastSection(True)

        layout.addLayout(self.searchLayout)
        layout.addWidget(self.resultsTable)

        # Add View Detail and Add New Patient Info buttons
        self.buttonLayout = QHBoxLayout()
        self.viewDetailButton = QPushButton("View Detail")
        self.addPatientInfoButton = QPushButton("Add New Patient Info")
        self.buttonLayout.addWidget(self.viewDetailButton)
        self.buttonLayout.addWidget(self.addPatientInfoButton)

        button_width = 200
        button_height = 50
        self.viewDetailButton.setFixedSize(button_width, button_height)
        self.addPatientInfoButton.setFixedSize(button_width, button_height)

        self.buttonLayout.addWidget(self.viewDetailButton)
        self.buttonLayout.addWidget(self.addPatientInfoButton)

        layout.addLayout(self.buttonLayout)

        self.searchButton.clicked.connect(self.search_history)



    def search_history(self):
        name = self.searchLineEdit.text().strip()
        if name:
            self.resultsTable.setRowCount(0)
            matching_entries = collection.find({"name": name})
            for entry in matching_entries:
                name = entry.get("name", "")
                visit_date = entry.get("date_of_visit", "")
                birth_date = entry.get("date_of_birth", "")
                bone = entry.get("Bone", "")
                fracture = entry.get("Fracture", "")
                notes = entry.get("Notes", "")

                row_position = self.resultsTable.rowCount()

                self.resultsTable.insertRow(row_position)
                self.resultsTable.setItem(row_position, 0, QTableWidgetItem(name))
                self.resultsTable.setItem(row_position, 1, QTableWidgetItem(visit_date))
                self.resultsTable.setItem(row_position, 2, QTableWidgetItem(birth_date))
                self.resultsTable.setItem(row_position, 3, QTableWidgetItem(bone))
                self.resultsTable.setItem(row_position, 4, QTableWidgetItem(fracture))
                self.resultsTable.setItem(row_position, 5, QTableWidgetItem(notes))


# Example usage:
if __name__ == "__main__":
    app = QApplication([])
    history_search_page = HistorySearchPage()
    history_search_page.show()
    app.exec()
