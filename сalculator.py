from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(333, 510)
        Calculator.setStyleSheet("background-color: rgb(76, 76, 76);")
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_formulas = QtWidgets.QPushButton(self.centralwidget)
        self.btn_formulas.setGeometry(QtCore.QRect(10, 90, 151, 61))
        self.btn_formulas.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"    \n"
"    \n"
"}")
        self.btn_formulas.setObjectName("btn_formulas")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 311, 71))
        self.label.setStyleSheet("font: 81 20pt \"Montserrat ExtraBold\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.btn_erase_everything = QtWidgets.QPushButton(self.centralwidget)
        self.btn_erase_everything.setGeometry(QtCore.QRect(170, 90, 71, 61))
        self.btn_erase_everything.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"    \n"
"    \n"
"}")
        self.btn_erase_everything.setObjectName("btn_erase_everything")
        self.btn_erase = QtWidgets.QPushButton(self.centralwidget)
        self.btn_erase.setGeometry(QtCore.QRect(250, 90, 71, 61))
        self.btn_erase.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"    \n"
"    \n"
"}")
        self.btn_erase.setObjectName("btn_erase")
        self.btn_division = QtWidgets.QPushButton(self.centralwidget)
        self.btn_division.setGeometry(QtCore.QRect(250, 160, 71, 61))
        self.btn_division.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 170, 127);\n"
"    \n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 141, 103);\n"
"    \n"
"    \n"
"}")
        self.btn_division.setObjectName("btn_division")
        self.btn_1_div = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1_div.setGeometry(QtCore.QRect(10, 160, 71, 61))
        self.btn_1_div.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"    \n"
"    \n"
"}")
        self.btn_1_div.setObjectName("btn_1_div")
        self.btn_in_squae = QtWidgets.QPushButton(self.centralwidget)
        self.btn_in_squae.setGeometry(QtCore.QRect(90, 160, 71, 61))
        self.btn_in_squae.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"    \n"
"    \n"
"}")
        self.btn_in_squae.setObjectName("btn_in_squae")
        self.btn_percent = QtWidgets.QPushButton(self.centralwidget)
        self.btn_percent.setGeometry(QtCore.QRect(170, 160, 71, 61))
        self.btn_percent.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"    \n"
"    \n"
"}")
        self.btn_percent.setObjectName("btn_percent")
        self.btn_multiplication = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multiplication.setGeometry(QtCore.QRect(250, 230, 71, 61))
        self.btn_multiplication.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 170, 127);\n"
"    \n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 141, 103);\n"
"    \n"
"    \n"
"}")
        self.btn_multiplication.setObjectName("btn_multiplication")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(10, 230, 71, 61))
        self.btn_7.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"    \n"
"    \n"
"}")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(90, 230, 71, 61))
        self.btn_8.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"    \n"
"    \n"
"}")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(170, 230, 71, 61))
        self.btn_9.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"    \n"
"    \n"
"}")
        self.btn_9.setObjectName("btn_9")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(250, 300, 71, 61))
        self.btn_minus.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 170, 127);\n"
"    \n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 141, 103);\n"
"    \n"
"    \n"
"}")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(10, 300, 71, 61))
        self.btn_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"    \n"
"    \n"
"}")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(90, 300, 71, 61))
        self.btn_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"    \n"
"    \n"
"}")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(170, 300, 71, 61))
        self.btn_6.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"    \n"
"    \n"
"}")
        self.btn_6.setObjectName("btn_6")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(90, 370, 71, 61))
        self.btn_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"    \n"
"    \n"
"}")
        self.btn_2.setObjectName("btn_2")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(250, 370, 71, 61))
        self.btn_plus.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 170, 127);\n"
"    \n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 141, 103);\n"
"    \n"
"    \n"
"}")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(170, 370, 71, 61))
        self.btn_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"    \n"
"    \n"
"}")
        self.btn_3.setObjectName("btn_3")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(10, 370, 71, 61))
        self.btn_1.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"    \n"
"    \n"
"}")
        self.btn_1.setObjectName("btn_1")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(10, 440, 151, 61))
        self.btn_0.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"    \n"
"    \n"
"}")
        self.btn_0.setObjectName("btn_0")
        self.btn_point = QtWidgets.QPushButton(self.centralwidget)
        self.btn_point.setGeometry(QtCore.QRect(170, 440, 71, 61))
        self.btn_point.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(204, 204, 204);\n"
"    \n"
"    \n"
"}")
        self.btn_point.setObjectName("btn_point")
        self.btn_result = QtWidgets.QPushButton(self.centralwidget)
        self.btn_result.setGeometry(QtCore.QRect(250, 440, 71, 61))
        self.btn_result.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 170, 127);\n"
"    \n"
"    font: 81 12pt \"Montserrat ExtraBold\";    \n"
"    border-radius: 5;\n"
"    color: white\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 141, 103);\n"
"    \n"
"    \n"
"}")
        self.btn_result.setObjectName("btn_result")
        Calculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Fatima"))
        self.btn_formulas.setText(_translate("Calculator", "Формулы"))
        self.label.setText(_translate("Calculator", "0"))
        self.btn_erase_everything.setText(_translate("Calculator", "C"))
        self.btn_erase.setText(_translate("Calculator", "<-"))
        self.btn_division.setText(_translate("Calculator", "/"))
        self.btn_1_div.setText(_translate("Calculator", "1/x"))
        self.btn_in_squae.setText(_translate("Calculator", "X2"))
        self.btn_percent.setText(_translate("Calculator", "%"))
        self.btn_multiplication.setText(_translate("Calculator", "*"))
        self.btn_7.setText(_translate("Calculator", "7"))
        self.btn_8.setText(_translate("Calculator", "8"))
        self.btn_9.setText(_translate("Calculator", "9"))
        self.btn_minus.setText(_translate("Calculator", "-"))
        self.btn_4.setText(_translate("Calculator", "4"))
        self.btn_5.setText(_translate("Calculator", "5"))
        self.btn_6.setText(_translate("Calculator", "6"))
        self.btn_2.setText(_translate("Calculator", "2"))
        self.btn_plus.setText(_translate("Calculator", "+"))
        self.btn_3.setText(_translate("Calculator", "3"))
        self.btn_1.setText(_translate("Calculator", "1"))
        self.btn_0.setText(_translate("Calculator", "0"))
        self.btn_point.setText(_translate("Calculator", "."))
        self.btn_result.setText(_translate("Calculator", "Result"))
        self.add_functions()

    def add_functions(self):
        #NumPad
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))

        #Классические знаки действия
        self.btn_multiplication.clicked.connect(lambda: self.write_number(self.btn_multiplication.text()))
        self.btn_division.clicked.connect(lambda: self.write_number(self.btn_division.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
        self.btn_percent.clicked.connect(lambda: self.write_number(self.btn_percent.text()))
        self.btn_point.clicked.connect(lambda: self.write_number(self.btn_point.text()))
        self.btn_erase_everything.clicked.connect(self.erase)

        #Результат
        self.btn_result.clicked.connect(self.result)

    # Функция, которая выводит нажатия на монитор
    def write_number(self, number):
        if self.label.text() == "0":
            self.label.setText(number)
        else:
            self.label.setText(self.label.text() + number)

    # Функция, которая стерает строку результата
    def erase(self):
        self.label.setText("0")

    # Функция, результат
    def result(self):
        res = eval(self.label.text())
        self.label.setText(str(res))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec())