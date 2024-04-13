from PySide6.QtCore import QRect, QCoreApplication
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QMenuBar, QMenu, QFileDialog
from mainPage import Ui_mainPage  # Assuming mainPage is another UI file

class ui_firstPageRevised(object):
    def openWindow(self):
        self.window = QMainWindow()
        self.ui = Ui_mainPage()
        self.ui.setupUi(self.window)
        self.window.show()

    def openFileManager(self):
        fileChosen, _ = QFileDialog.getOpenFileName(self.window, "Open Image", "~/", "All Files(*)", "", QFileDialog.ReadOnly)

        if fileChosen:
            self.label.setText(str(fileChosen))

    def setupUi(self, FirstPage):
        if not FirstPage.objectName():
            FirstPage.setObjectName("FirstPage")
        FirstPage.resize(800, 600)

        self.centralwidget = QWidget(FirstPage)
        self.centralwidget.setObjectName("centralwidget")

        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setObjectName("nameLabel")
        self.nameLabel.setGeometry(QRect(250, 50, 301, 45))
        font = QFont()
        font.setPointSize(45)
        self.nameLabel.setFont(font)

        self.descLabel = QLabel(self.centralwidget)
        self.descLabel.setObjectName("descLabel")
        self.descLabel.setGeometry(QRect(270, 110, 260, 19))

        self.iconLabel = QLabel(self.centralwidget)
        self.iconLabel.setObjectName("iconLabel")
        self.iconLabel.setGeometry(QRect(240, 140, 300, 271))
        self.iconLabel.setPixmap(QPixmap("noun-bone-3858505.png"))

        self.uploadButton = QPushButton(self.centralwidget)
        self.uploadButton.setObjectName("uploadButton")
        self.uploadButton.setGeometry(QRect(320, 440, 150, 30))
        self.uploadButton.clicked.connect(self.openFileManager)

        self.reloadButton = QPushButton(self.centralwidget)
        self.reloadButton.setObjectName("reloadButton")
        self.reloadButton.setGeometry(QRect(320, 490, 150, 30))
        self.reloadButton.clicked.connect(self.openWindow)

        self.aboutButton = QPushButton(self.centralwidget)
        self.aboutButton.setGeometry(QRect(680, 520, 113, 32))
        self.aboutButton.setObjectName("aboutButton")
        self.aboutButton.clicked.connect(self.openWindow)

        FirstPage.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(FirstPage)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))

        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")

        FirstPage.setMenuBar(self.menubar)

        self.statusbar = FirstPage.statusBar()
        self.statusbar.setObjectName("statusbar")

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(FirstPage)

    def retranslateUi(self, FirstPage):
        FirstPage.setWindowTitle(QCoreApplication.translate("FirstPage", "FirstPage", None))
        self.nameLabel.setText(QCoreApplication.translate("FirstPage", "BoneVision", None))
        self.descLabel.setText(QCoreApplication.translate("FirstPage", "A Bone Fracture Detection Application", None))
        self.uploadButton.setText(QCoreApplication.translate("FirstPage", "Upload X-Ray", None))
        self.reloadButton.setText(QCoreApplication.translate("FirstPage", "Reload X-Ray", None))
        self.aboutButton.setText(QCoreApplication.translate("FirstPage", "About", None))
        self.menuFile.setTitle(QCoreApplication.translate("FirstPage", "File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("FirstPage", "About", None))
