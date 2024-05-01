from PySide6.QtCore import QObject, Slot, QCoreApplication
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
import bcrypt
import os

class ui_LoginWindow(QMainWindow):
    curr_username = ''
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 600)

        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QWidget(self.centralwidget)
        self.groupBox.setGeometry(120, 50, 581, 421)

        self.UsernameLabel = QLabel(self.groupBox)
        self.UsernameLabel.setGeometry(140, 190, 81, 16)
        self.UsernameLabel.setText("Username")

        self.PasswordLabel = QLabel(self.groupBox)
        self.PasswordLabel.setGeometry(140, 240, 71, 16)
        self.PasswordLabel.setText("Password")

        self.LoginLabel = QLabel(self.groupBox)
        self.LoginLabel.setGeometry(200, 110, 251, 31)
        self.LoginLabel.setText("Welcome to Bone Vision")

        self.lineEditUser = QLineEdit(self.groupBox)
        self.lineEditUser.setGeometry(240, 190, 161, 21)

        self.lineEditPass = QLineEdit(self.groupBox)
        self.lineEditPass.setGeometry(240, 240, 161, 21)
        self.lineEditPass.setEchoMode(QLineEdit.Password)  # Set password echo mode

        self.RegisterBtn = QPushButton(self.groupBox)
        self.RegisterBtn.setGeometry(170, 330, 113, 32)
        self.RegisterBtn.setText("Register")

        self.LoginBtn = QPushButton(self.groupBox)
        self.LoginBtn.setGeometry(320, 330, 113, 32)
        self.LoginBtn.setText("Login")
        self.LoginBtn.clicked.connect(self.handleLogin)

        LoginWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(LoginWindow)

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", "Login"))
        self.RegisterBtn.setText(QCoreApplication.translate("LoginWindow", "Register"))
        self.LoginBtn.setText(QCoreApplication.translate("LoginWindow", "Login"))

    @Slot()
    def handleLogin(self):
        username = self.lineEditUser.text().strip()
        password = self.lineEditPass.text().strip()

        if self.authenticate_user(username, password):
            self.curr_username = username
            self.openFirstPage()
        else:
            QMessageBox.warning(None, "Login Failed", "Username or password does not match our records.")

    def authenticate_user(self, username, password):
        credentials_file = "user_credentials.txt"

        if os.path.exists(credentials_file):
            with open(credentials_file, "r") as file:
                for line in file:
                    stored_username, stored_password = line.strip().split(",")
                    if username == stored_username:
                        # Check if the provided password matches the stored hashed password
                        if bcrypt.checkpw(password.encode(), stored_password.encode()):
                            return True
        return False

    def openFirstPage(self):
        from ui_firstPageRevised import ui_firstPageRevised
        self.first_page_window = QMainWindow()
        self.first_page_ui = ui_firstPageRevised()
        self.first_page_ui.setUserName(self.curr_username)
        self.first_page_ui.setupUi(self.first_page_window)
        self.first_page_window.show()
        self.centralwidget.window().close()