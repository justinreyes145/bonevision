from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
import bcrypt

def save_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    with open('user_credentials.txt', 'a') as file:
        file.write(f"{username},{hashed_password.decode()}\n")

class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register")
        self.setGeometry(200, 200, 400, 250)  # Set window position and size


        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.usernameLabel = QLabel("Username:", self.centralWidget)
        self.usernameLabel.move(50, 50)
        self.usernameLineEdit = QLineEdit(self.centralWidget)
        self.usernameLineEdit.setGeometry(150, 50, 200, 30)

        self.passwordLabel = QLabel("Password:", self.centralWidget)
        self.passwordLabel.move(50, 100)
        self.passwordLineEdit = QLineEdit(self.centralWidget)
        self.passwordLineEdit.setGeometry(150, 100, 200, 30)
        self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.registerButton = QPushButton("Register", self.centralWidget)
        self.registerButton.setGeometry(150, 150, 100, 30)
        self.registerButton.clicked.connect(self.register_user)

    def register_user(self):
        username = self.usernameLineEdit.text().strip()
        password = self.passwordLineEdit.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Please enter both username and password.")
            return

        # Save user credentials with hashed password
        save_user(username, password)

        # Inform user that registration was successful
        QMessageBox.information(self, "Success", "Registration successful!")

        # Clear input fields after successful registration
        self.usernameLineEdit.clear()
        self.passwordLineEdit.clear()
