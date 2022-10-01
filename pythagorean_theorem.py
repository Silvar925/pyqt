from PyQt6 import QtCore, QtGui, QtWidgets
from math import sqrt


class Ui_Pythagorean_Theorem(object):
    def setupUi(self, Pythagorean_Theorem):
        Pythagorean_Theorem.setObjectName("Pythagorean_Theorem")
        Pythagorean_Theorem.resize(348, 391)
        Pythagorean_Theorem.setStyleSheet("background-color: rgb(76, 76, 76);")
        self.centralwidget = QtWidgets.QWidget(Pythagorean_Theorem)
        self.centralwidget.setObjectName("centralwidget")
        self.first_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.first_lineEdit.setGeometry(QtCore.QRect(20, 130, 311, 51))
        self.first_lineEdit.setStyleSheet("font: 81 15pt \"Montserrat ExtraBold\";\n"
"background-color: rgb(255, 255, 255);")
        self.first_lineEdit.setPlaceholderText("Первый катет")
        self.first_lineEdit.setObjectName("first_lineEdit")
        self.result = QtWidgets.QPushButton(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(180, 310, 151, 51))
        self.result.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"        \n"
"}")
        self.result.setObjectName("result")
        self.second_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.second_lineEdit.setGeometry(QtCore.QRect(20, 190, 311, 51))
        self.second_lineEdit.setStyleSheet("font: 81 15pt \"Montserrat ExtraBold\";\n"
"background-color: rgb(255, 255, 255);")
        self.second_lineEdit.setObjectName("second_lineEdit")
        self.second_lineEdit.setPlaceholderText("Второй катет")
        self.text_p = QtWidgets.QLabel(self.centralwidget)
        self.text_p.setGeometry(QtCore.QRect(70, 10, 241, 51))
        self.text_p.setStyleSheet("font: 81 15pt \"Montserrat ExtraBold\";\n"
"color: rgb(255, 255, 255);")
        self.text_p.setObjectName("text_p")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(20, 70, 311, 51))
        self.result_label.setStyleSheet("font: 81 15pt \"Montserrat ExtraBold\";\n"
"color: rgb(255, 255, 255);")
        self.result_label.setObjectName("result_label")
        self.third_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.third_lineEdit.setGeometry(QtCore.QRect(20, 250, 311, 51))
        self.third_lineEdit.setStyleSheet("font: 81 15pt \"Montserrat ExtraBold\";\n"
"background-color: rgb(255, 255, 255);")
        self.third_lineEdit.setPlaceholderText("Гипотенуза")
        self.third_lineEdit.setObjectName("third_lineEdit")
        self.more = QtWidgets.QPushButton(self.centralwidget)
        self.more.setGeometry(QtCore.QRect(20, 310, 151, 51))
        self.more.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 170, 127);\n"
"    \n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 141, 103);    \n"
"}")
        self.more.setObjectName("more")
        Pythagorean_Theorem.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(Pythagorean_Theorem)
        self.statusBar.setObjectName("statusBar")
        Pythagorean_Theorem.setStatusBar(self.statusBar)

        self.retranslateUi(Pythagorean_Theorem)
        QtCore.QMetaObject.connectSlotsByName(Pythagorean_Theorem)

        self.result.clicked.connect(self.add_functions)

    def retranslateUi(self, Pythagorean_Theorem):
        _translate = QtCore.QCoreApplication.translate
        Pythagorean_Theorem.setWindowTitle(_translate("Pythagorean_Theorem", "Pythagorean Theorem"))
        self.result.setText(_translate("Pythagorean_Theorem", "Результат"))
        self.text_p.setText(_translate("Pythagorean_Theorem", "Теорема Пифагора"))
        self.result_label.setText(_translate("Pythagorean_Theorem", "0"))
        self.more.setText(_translate("Pythagorean_Theorem", "Подробнее"))

    def add_functions(self):
        cat1 = self.first_lineEdit.text()
        cat2 = self.second_lineEdit.text()
        hyp = self.third_lineEdit.text()

        if cat1 == "0":
            cat1 = sqrt(int(hyp) ** 2 - int(cat2) ** 2)
            self.result_label.setText(str(cat1))
        elif cat2 == "0":
            cat2 = sqrt(int(hyp) ** 2 - int(cat1) ** 2)
            self.result_label.setText(str(cat2))
        elif hyp == "0":
            hyp = int(cat1) ** 2 + int(cat2) ** 2
            self.result_label.setText(str(hyp))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pythagorean_Theorem = QtWidgets.QMainWindow()
    ui = Ui_Pythagorean_Theorem()
    ui.setupUi(Pythagorean_Theorem)
    Pythagorean_Theorem.show()
    sys.exit(app.exec())