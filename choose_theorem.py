from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Choose_theorem(object):
    def setupUi(self, Choose_theorem):
        Choose_theorem.setObjectName("Choose_theorem")
        Choose_theorem.resize(303, 328)
        Choose_theorem.setStyleSheet("background-color: rgb(76, 76, 76);")
        self.centralwidget = QtWidgets.QWidget(Choose_theorem)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 160, 261, 71))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 170, 127);\n"
"    \n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 141, 103);    \n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 80, 261, 71))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"        \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 251, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 17pt \"Montserrat Black\";")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 240, 261, 71))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"        \n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        Choose_theorem.setCentralWidget(self.centralwidget)

        self.retranslateUi(Choose_theorem)
        QtCore.QMetaObject.connectSlotsByName(Choose_theorem)

    def retranslateUi(self, Choose_theorem):
        _translate = QtCore.QCoreApplication.translate
        Choose_theorem.setWindowTitle(_translate("Choose_theorem", "Choose a theorem"))
        self.pushButton.setText(_translate("Choose_theorem", "Теорема Фалеса"))
        self.pushButton_2.setText(_translate("Choose_theorem", "Теорма Пифагора"))
        self.label.setText(_translate("Choose_theorem", "Выберите теорему"))
        self.pushButton_3.setText(_translate("Choose_theorem", "Теорема Виета"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Choose_theorem = QtWidgets.QMainWindow()
    ui = Ui_Choose_theorem()
    ui.setupUi(Choose_theorem)
    Choose_theorem.show()
    sys.exit(app.exec())
