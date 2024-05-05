from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from dbconn import *


class HistorySearchPage(QMainWindow):
    curr_username = ''

    def setUserName(self, username):
        self.curr_username = username

    def __init__(self):
        super().__init__()
        self.setWindowTitle("History Search Page")
        self.resize(800, 600)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        # self.setup_ui(self)

    def setup_ui(self, window):
        if not window.objectName():
            window.setObjectName(u"window")
        window.setWindowTitle("History Search Page")
        window.resize(800, 600)

        window.centralwidget = QWidget(self)
        window.setCentralWidget(self.centralwidget)

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
        self.resultsTable.setColumnCount(7)
        self.resultsTable.setHorizontalHeaderLabels(["Test ID", "Name", "Date of Visit", "Birth Date", "Bone", "Fracture", "Notes"])
        self.resultsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.resultsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.resultsTable.horizontalHeader().setStretchLastSection(True)
        self.resultsTable.verticalHeader().setVisible(False)
        self.resultsTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.resultsTable.setSelectionMode(QAbstractItemView.SingleSelection)

        layout.addLayout(self.searchLayout)
        layout.addWidget(self.resultsTable)

        # Add View Detail and Add New Patient Info buttons
        self.buttonLayout = QHBoxLayout()

        self.viewDetailButton = QPushButton("View Detail")
        self.viewDetailButton.clicked.connect(self.view_detail_clicked)
        # self.addPatientInfoButton = QPushButton("Add New Patient Info")
        self.buttonLayout.addWidget(self.viewDetailButton)
        # self.buttonLayout.addWidget(self.addPatientInfoButton)
        button_width = 200
        button_height = 50
        self.viewDetailButton.setFixedSize(button_width, button_height)

        layout.addLayout(self.buttonLayout)

        self.searchButton.clicked.connect(self.callDB)

    def view_detail_clicked(self):
        selected = self.resultsTable.selectedItems()
        print(selected[1].text(), selected[2].text(), selected[3].text(),
              selected[4].text(), selected[5].text(), selected[6].text())

    def callDB(self):
        query = find_name(self.searchLineEdit.text(), self.curr_username)
        result_row = 0
        self.resultsTable.setRowCount(len(query))
        for row in query:
            self.resultsTable.setItem(result_row, 0, QTableWidgetItem(f'{row[0]}'))
            self.resultsTable.setItem(result_row, 1, QTableWidgetItem(row[2]))
            self.resultsTable.setItem(result_row, 2, QTableWidgetItem(row[3]))
            self.resultsTable.setItem(result_row, 3, QTableWidgetItem(row[4]))
            self.resultsTable.setItem(result_row, 4, QTableWidgetItem(row[5]))
            self.resultsTable.setItem(result_row, 5, QTableWidgetItem(row[6]))
            self.resultsTable.setItem(result_row, 6, QTableWidgetItem(row[8]))
            result_row += 1

# Example usage:
if __name__ == "__main__":
    app = QApplication([])
    history_search_page = HistorySearchPage()
    history_search_page.show()
    app.exec()
