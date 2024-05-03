from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from dbconn import *


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
        self.searchLabel = QtWidgets.QLabel("Enter Name:")
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
        # self.addPatientInfoButton = QPushButton("Add New Patient Info")
        self.buttonLayout.addWidget(self.viewDetailButton)
        # self.buttonLayout.addWidget(self.addPatientInfoButton)

        layout.addLayout(self.buttonLayout)

        self.searchButton.clicked.connect(self.callDB)

    def callDB(self):
        query = find_name(self.searchLineEdit.text(), 'cat')
        result_row = 0
        self.resultsTable.setRowCount(len(query))
        for row in query:
            self.resultsTable.setItem(result_row, 0, QTableWidgetItem(row[2]))
            self.resultsTable.setItem(result_row, 1, QTableWidgetItem(row[3]))
            self.resultsTable.setItem(result_row, 2, QTableWidgetItem(row[4]))
            self.resultsTable.setItem(result_row, 3, QTableWidgetItem(row[5]))
            self.resultsTable.setItem(result_row, 4, QTableWidgetItem(row[6]))
            self.resultsTable.setItem(result_row, 5, QTableWidgetItem(row[8]))
            result_row += 1
            #Need to reset a value here

# Example usage:
if __name__ == "__main__":
    app = QApplication([])
    history_search_page = HistorySearchPage()
    history_search_page.show()
    app.exec()
