import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication
from ui_firstPageRevised import Ui_MainWindow


class firstPage(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    page = QtWidgets.QApplication([])
    pageWindow = firstPage()
    pageWindow.show()
    sys.exit(page.exec_())
