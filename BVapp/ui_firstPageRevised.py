from PySide6.QtCore import QRect, QCoreApplication, QMetaObject
from PySide6.QtGui import QFont, QPixmap, QAction
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton
from mainPage import Ui_mainPage  # Assuming mainPage is another UI file
from history import HistorySearchPage


class ui_firstPageRevised(object):
    curr_username = ''

    def setUserName(self, username):
        self.curr_username = username


    def openNewCaseWindow(self):
        self.window = QMainWindow()
        self.ui = Ui_mainPage()
        self.ui.setUserName(self.curr_username)
        self.ui.setupUi(self.window)
        self.window.show()
        self.centralwidget.window().close()

    def openExistingCaseWindow(self):
        self.window = QMainWindow()
        self.ui = HistorySearchPage()
        self.ui.setUserName(self.curr_username)
        self.ui.setup_ui(self.window)
        self.window.show()
        self.centralwidget.window().close()

    def logOut(self):
        from ui_LoginWindow import ui_LoginWindow  # avoid circular import
        self.login_page_window = QMainWindow()
        self.ui_login_page = ui_LoginWindow()
        self.ui_login_page.setupUi(self.login_page_window)
        self.login_page_window.show()
        self.centralwidget.window().close()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionDevs = QAction(MainWindow)
        self.actionDevs.setObjectName(u"actionDevs")
        self.actionReport_Bug = QAction(MainWindow)
        self.actionReport_Bug.setObjectName(u"actionReport_Bug")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(250, 50, 301, 45))
        font = QFont()
        font.setPointSize(40)
        self.nameLabel.setFont(font)
        self.descLabel = QLabel(self.centralwidget)
        self.descLabel.setObjectName(u"descLabel")
        self.descLabel.setGeometry(QRect(270, 110, 260, 19))
        self.iconLabel = QLabel(self.centralwidget)
        self.iconLabel.setObjectName(u"iconLabel")
        self.iconLabel.setGeometry(QRect(240, 140, 300, 271))
        self.iconLabel.setPixmap(QPixmap("noun-bone-3858505.png"))
        self.existingCaseButton = QPushButton(self.centralwidget)
        self.existingCaseButton.setObjectName(u"existingCaseButton")
        self.existingCaseButton.clicked.connect(self.openExistingCaseWindow)
        self.existingCaseButton.setGeometry(QRect(320, 440, 150, 30))
        self.newCaseButton = QPushButton(self.centralwidget)
        self.newCaseButton.setObjectName(u"newCaseButton")
        self.newCaseButton.clicked.connect(self.openNewCaseWindow)
        self.newCaseButton.setGeometry(QRect(320, 490, 150, 30))
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.clicked.connect(self.logOut)
        self.backButton.setGeometry(QRect(320, 540, 150, 30))
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionDevs.setText(QCoreApplication.translate("MainWindow", u"Devs", None))
        self.actionReport_Bug.setText(QCoreApplication.translate("MainWindow", u"Report Bug", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"BoneVision", None))
        self.descLabel.setText(QCoreApplication.translate("MainWindow", u"A Bone Fracture Detection Application", None))
        self.iconLabel.setText("")
        self.existingCaseButton.setText(QCoreApplication.translate("MainWindow", u"Existing Case", None))
        self.newCaseButton.setText(QCoreApplication.translate("MainWindow", u"New Case", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))

        print(self.curr_username)
    # retranslateUi
