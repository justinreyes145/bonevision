import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from ui_LoginWindow import ui_LoginWindow
from ui_firstPageRevised import ui_firstPageRevised
from register_window import RegisterWindow

sys.argv += ['-platform', 'windows:darkmode=2']

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui_LoginWindow()
        self.ui.setupUi(self)

class FirstPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui_firstPageRevised()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())