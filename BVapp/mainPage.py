from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QFileDialog
from datetime import datetime
import shutil
import os

from dbconn import insert_one, update_img_path
from image_enhancement import process_img
import string
from classifier import predict_image


class Ui_mainPage(object):
    curr_username = ''

    def go_back_btn(self):
        from ui_firstPageRevised import ui_firstPageRevised  # avoid circular import
        self.first_page_window = QMainWindow()
        self.ui_first_page = ui_firstPageRevised()
        self.ui_first_page.setUserName(self.curr_username)
        self.ui_first_page.setupUi(self.first_page_window)
        self.first_page_window.show()
        self.centralwidget.window().close()

    def scan_clicked(self):
        if hasattr(self, 'uploaded_image_path'):
            predict_image(self.outputPane)
        else:
            QMessageBox.warning(self.centralwidget, "Warning", "No image uploaded!", QMessageBox.Ok)


    def setUserName(self, username):
        self.curr_username = username

    def saveStringInfo(self):
        patientName = self.nameField.toPlainText() #Use this as a template for the rest of the fields
        filename = "%s.txt" % patientName
        with open(filename,'w') as patientProfile:
            patientProfile.write(patientName) #We are gonna write the information like this

    def setupUi(self, mainPage):
        if not mainPage.objectName():
            mainPage.setObjectName(u"mainPage")
        mainPage.resize(1100, 600)
        self.actionNew = QAction(mainPage)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(mainPage)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(mainPage)
        self.actionClose.setObjectName(u"actionClose")
        self.centralwidget = QWidget(mainPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.outputPane = QTextBrowser(self.centralwidget)
        self.outputPane.setObjectName(u"outputPane")
        self.outputPane.setGeometry(QRect(325, 10, 291, 471))
        self.imagePane = QLabel(self.centralwidget)
        self.imagePane.setObjectName(u"imagePane")
        self.imagePane.setGeometry(QRect(650, 10, 381, 475))
        self.imagePane.setPixmap(QPixmap("Resources/IMG0000019-1.jpg"))
        self.uploadButton = QPushButton(self.centralwidget)
        self.uploadButton.setObjectName(u"uploadButton")
        self.uploadButton.clicked.connect(self.upload_clicked)
        self.uploadButton.setGeometry(QRect(650, 510, 121, 27))
        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(900, 510, 121, 27))  # Adjusted position
        self.nameField = QTextEdit(self.centralwidget)
        self.nameField.setObjectName(u"nameField")
        self.nameField.setGeometry(QRect(10, 50, 291, 31))
        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(10, 20, 100, 19))
        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setGeometry(QRect(10, 90, 100, 19))
        self.bdateLabel = QLabel(self.centralwidget)
        self.bdateLabel.setObjectName(u"bdateLabel")
        self.bdateLabel.setGeometry(QRect(10, 150, 100, 19))
        self.dateMonth = QTextEdit(self.centralwidget)
        self.dateMonth.setObjectName(u"dateMonth")
        self.dateMonth.setGeometry(QRect(10, 110, 30, 30))
        self.dateDay = QTextEdit(self.centralwidget)
        self.dateDay.setObjectName(u"dateDay")
        self.dateDay.setGeometry(QRect(55, 110, 30, 30))
        self.dateYear = QTextEdit(self.centralwidget)
        self.dateYear.setObjectName(u"dateYear")
        self.dateYear.setGeometry(QRect(100, 110, 60, 30))
        self.bdateMonth = QTextEdit(self.centralwidget)
        self.bdateMonth.setObjectName(u"bdateMonth")
        self.bdateMonth.setGeometry(QRect(10, 170, 30, 30))
        self.bdateDay = QTextEdit(self.centralwidget)
        self.bdateDay.setObjectName(u"bdateDay")
        self.bdateDay.setGeometry(QRect(55, 170, 30, 30))
        self.bdateYear = QTextEdit(self.centralwidget)
        self.bdateYear.setObjectName(u"bdateYear")
        self.bdateYear.setGeometry(QRect(100, 170, 60, 30))
        self.dateDash1 = QLabel(self.centralwidget)
        self.dateDash1.setObjectName(u"dateDash1")
        self.dateDash1.setGeometry(QRect(45, 115, 12, 19))
        self.dateDash2 = QLabel(self.centralwidget)
        self.dateDash2.setObjectName(u"dateDash2")
        self.dateDash2.setGeometry(QRect(90, 115, 15, 19))
        self.bdateDash1 = QLabel(self.centralwidget)
        self.bdateDash1.setObjectName(u"bdateDash1")
        self.bdateDash1.setGeometry(QRect(45, 175, 12, 19))
        self.bdateDash2 = QLabel(self.centralwidget)
        self.bdateDash2.setObjectName(u"bdateDash2")
        self.bdateDash2.setGeometry(QRect(90, 175, 12, 19))
        self.contextPane = QTextEdit(self.centralwidget)
        self.contextPane.setObjectName(u"contextPane")
        self.contextPane.setGeometry(QRect(10, 240, 300, 241))
        self.notesLabel = QLabel(self.centralwidget)
        self.notesLabel.setObjectName(u"notesLabel")
        self.notesLabel.setGeometry(QRect(10, 210, 150, 19))

        mainPage.setCentralWidget(self.centralwidget)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setGeometry(QRect(10, 510, 121, 27))
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(self.go_back_btn)

        self.scanButton = QPushButton(self.centralwidget)
        self.scanButton.setObjectName(u"scanButton")
        self.scanButton.setGeometry(QRect(775, 510, 121, 27))
        self.scanButton.clicked.connect(self.scan_clicked)


        self.retranslateUi(mainPage)

        QMetaObject.connectSlotsByName(mainPage)

        self.saveButton.clicked.connect(self.save_clicked)  # Connect the save button to its function

    def load_values(self, l_name, l_v_date, l_b_date, bone, frac, notes, img_path):
        self.nameField.setText(l_name)
        v_date = l_v_date.split('-')
        self.dateDay.setText(v_date[2])
        self.dateMonth.setText(v_date[1])
        self.dateYear.setText(v_date[0])
        b_date = l_b_date.split('-')
        self.bdateDay.setText(b_date[2])
        self.bdateMonth.setText(b_date[1])
        self.bdateYear.setText(b_date[0])

        self.contextPane.setText(notes)
        self.uploaded_image_path = img_path
        pixmap = QPixmap(img_path)
        scaled_pixmap = pixmap.scaled(self.imagePane.size(), Qt.KeepAspectRatio)
        self.imagePane.setPixmap(scaled_pixmap)

        result = f"{frac} chance of {bone} fracture"
        html_result = f'<div style="text-align: center; font-size: 50px;">{result}</div>'

        # update the output pane HTML with the result
        self.outputPane.setHtml(html_result)

        self.centralwidget.update()

    def upload_clicked(self):
        # Function to handle upload button click
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                new_image_path = file_paths[0]
                print(new_image_path)
                process_img(new_image_path)

                self.uploaded_image_path = new_image_path
                pixmap = QPixmap(new_image_path)
                scaled_pixmap = pixmap.scaled(self.imagePane.size(), Qt.KeepAspectRatio)
                self.imagePane.setPixmap(scaled_pixmap)
                self.centralwidget.update()


    def retranslateUi(self, mainPage):
        mainPage.setWindowTitle(QCoreApplication.translate("mainPage", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("mainPage", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("mainPage", u"Open", None))
        self.actionClose.setText(QCoreApplication.translate("mainPage", u"Close", None))

        self.outputPane.setHtml(QCoreApplication.translate("mainPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                       "p, li { white-space: pre-wrap; }\n"
                                                                       ".vertical-text { writing-mode: vertical-rl; }\n"  # Add this line for vertical text
                                                                       "</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal; text-align: center;\">\n"
                                                                       "<p class='vertical-text' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
                                                                       "<p class='vertical-text' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
                                                                       "<p class='vertical-text' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))



        self.imagePane.setText("")
        self.uploadButton.setText(QCoreApplication.translate("mainPage", u"Upload", None))

        self.saveButton.setText(QCoreApplication.translate("mainPage", u"Save", None))
        # Set text for save button
        self.nameField.setHtml(QCoreApplication.translate("mainPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                      "p, li { white-space: pre-wrap; }\n"
                                                                      "</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                                      "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">EX) John Smith</p>\n"
                                                                      "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.nameLabel.setText(QCoreApplication.translate("mainPage", u"Name: ", None))
        self.dateLabel.setText(QCoreApplication.translate("mainPage", u"Date of Visit: ", None))
        self.bdateLabel.setText(QCoreApplication.translate("mainPage", u"Date of Birth", None))
        self.dateMonth.setHtml(QCoreApplication.translate("mainPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                      "p, li { white-space: pre-wrap; }\n"
                                                                      "</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                                      "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12</p></body></html>", None))
        self.dateDay.setHtml(QCoreApplication.translate("mainPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                    "p, li { white-space: pre-wrap; }\n"
                                                                    "</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12</p></body></html>", None))
        self.dateYear.setHtml(QCoreApplication.translate("mainPage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                     "p, li { white-space: pre-wrap; }\n"
                                                                     "</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">12</p></body></html>", None))
        self.dateDash1.setText(QCoreApplication.translate("mainPage", u"/", None))
        self.dateDash2.setText(QCoreApplication.translate("mainPage", u"/", None))
        self.bdateDash1.setText(QCoreApplication.translate("mainPage", u"/", None))
        self.bdateDash2.setText(QCoreApplication.translate("mainPage", u"/", None))
        self.notesLabel.setText(QCoreApplication.translate("mainPage", u"Additional Notes: ", None))

        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))

        self.scanButton.setText(QCoreApplication.translate("mainPage", u"Scan Now", None))


        print(self.curr_username)

    def sanitize_filename(self,name):
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        return ''.join(c for c in name if c in valid_chars)

    def save_clicked(self):
        if self.outputPane.toPlainText().split().__len__() < 2:
            return
        name = self.sanitize_filename(self.nameField.toPlainText())
        date_of_visit = f"{self.dateYear.toPlainText()}-{self.dateMonth.toPlainText()}-{self.dateDay.toPlainText()}"
        date_of_birth = f"{self.bdateYear.toPlainText()}-{self.bdateMonth.toPlainText()}-{self.bdateDay.toPlainText()}"
        scan_result = self.outputPane.toPlainText().split()
        fracture_type = scan_result[0]
        fracture_location = scan_result[3]
        additional_notes = self.contextPane.toPlainText()

        test_num = insert_one(self.curr_username, name, date_of_visit, date_of_birth, fracture_location,
                              fracture_type, "", additional_notes)

        # Create a folder named 'download' if it doesn't exist
        if not os.path.exists('download'):
            os.makedirs('download')

        # Construct filenames using user's name and birthdate
        file_prefix = f"scan{test_num}"

        # Sanitize file prefix
        file_prefix = self.sanitize_filename(file_prefix)

        # Save the information into a text file
        txt_file_name = f"download/{file_prefix}_info.txt"
        with open(txt_file_name, 'w') as f:
            f.write(f"Name: {name}\n")
            f.write(f"Date of Visit: {date_of_visit}\n")
            f.write(f"Date of Birth: {date_of_birth}\n")
            f.write(f"Additional Notes:\n{additional_notes}")

        # Save the uploaded image to the 'download' folder
        if hasattr(self, 'uploaded_image_path'):  # Check if an image is uploaded
            # Construct image filename
            image_extension = os.path.splitext(self.uploaded_image_path)[1]
            image_name = f"download/{file_prefix}_image{image_extension}"
            shutil.copy(self.uploaded_image_path, image_name)
            update_img_path(test_num, image_name)

        # Show a message box indicating successful save
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Save Successful!")
        msgBox.setWindowTitle("Success")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
