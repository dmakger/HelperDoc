# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_HelperDoc(object):
    def setupUi(self, HelperDoc):
        HelperDoc.setObjectName("HelperDoc")
        HelperDoc.resize(990, 687)
        HelperDoc.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        HelperDoc.setAutoFillBackground(False)
        HelperDoc.setStyleSheet("background-color: #181818;")
        self.centralwidget = QtWidgets.QWidget(HelperDoc)
        self.centralwidget.setObjectName("centralwidget")
        self.add_row = QtWidgets.QPushButton(self.centralwidget)
        self.add_row.setGeometry(QtCore.QRect(500, 600, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.add_row.setFont(font)
        self.add_row.setStyleSheet("QPushButton {\n"
"    background-color: #2C2C2C;\n"
"    color: #fff;\n"
"    text-align: center;\n"
"    padding-bottom: 1px;\n"
"    border: 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #353535;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #3F3F3F;\n"
"}")
        self.add_row.setObjectName("add_row")
        self.suggest_input = QtWidgets.QLineEdit(self.centralwidget)
        self.suggest_input.setGeometry(QtCore.QRect(190, 50, 521, 31))
        self.suggest_input.setStyleSheet("QLineEdit {\n"
"    color: #fff;\n"
"    padding-left: 10px;\n"
"}")
        self.suggest_input.setText("")
        self.suggest_input.setObjectName("suggest_input")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(60, 110, 881, 461))
        self.table.setBaseSize(QtCore.QSize(0, 0))
        self.table.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.table.setStyleSheet("background-color: #fff;")
        self.table.setObjectName("table")
        self.table.setColumnCount(28)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(27, item)
        self.suggest_input_button = QtWidgets.QPushButton(self.centralwidget)
        self.suggest_input_button.setGeometry(QtCore.QRect(720, 50, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.suggest_input_button.setFont(font)
        self.suggest_input_button.setStyleSheet("QPushButton {\n"
"    background-color: #2C2C2C;\n"
"    color: #fff;\n"
"    text-align: center;\n"
"    border: 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #353535;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #3F3F3F;\n"
"}")
        self.suggest_input_button.setObjectName("suggest_input_button")
        self.remove_row = QtWidgets.QPushButton(self.centralwidget)
        self.remove_row.setGeometry(QtCore.QRect(380, 600, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.remove_row.setFont(font)
        self.remove_row.setStyleSheet("QPushButton {\n"
"    background-color: #2C2C2C;\n"
"    color: #fff;\n"
"    text-align: center;\n"
"    padding-bottom: 1px;\n"
"    border: 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #353535;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #3F3F3F;\n"
"}")
        self.remove_row.setObjectName("remove_row")
        HelperDoc.setCentralWidget(self.centralwidget)

        self.retranslateUi(HelperDoc)
        QtCore.QMetaObject.connectSlotsByName(HelperDoc)

    def retranslateUi(self, HelperDoc):
        _translate = QtCore.QCoreApplication.translate
        HelperDoc.setWindowTitle(_translate("HelperDoc", "MainWindow"))
        self.add_row.setText(_translate("HelperDoc", "Добавить"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("HelperDoc", "Наименование документа"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("HelperDoc", "Вид документа"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("HelperDoc", "Статус документа"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("HelperDoc", "Подтверждение утраты"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("HelperDoc", "Подтверждение обмена "))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("HelperDoc", "Подтверждение уничтожения"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("HelperDoc", "Уровень образования"))
        item = self.table.horizontalHeaderItem(7)
        item.setText(_translate("HelperDoc", "Серия документа"))
        item = self.table.horizontalHeaderItem(8)
        item.setText(_translate("HelperDoc", "Номер документа"))
        item = self.table.horizontalHeaderItem(9)
        item.setText(_translate("HelperDoc", "Дата выдачи"))
        item = self.table.horizontalHeaderItem(10)
        item.setText(_translate("HelperDoc", "Регистрационный номер"))
        item = self.table.horizontalHeaderItem(11)
        item.setText(_translate("HelperDoc", "Код профессии, специальности"))
        item = self.table.horizontalHeaderItem(12)
        item.setText(_translate("HelperDoc", "Наименование профессии, специальности"))
        item = self.table.horizontalHeaderItem(13)
        item.setText(_translate("HelperDoc", "Наименование квалификации"))
        item = self.table.horizontalHeaderItem(14)
        item.setText(_translate("HelperDoc", "Наименование образовательной  программы"))
        item = self.table.horizontalHeaderItem(15)
        item.setText(_translate("HelperDoc", "Год поступления"))
        item = self.table.horizontalHeaderItem(16)
        item.setText(_translate("HelperDoc", "Год окончания"))
        item = self.table.horizontalHeaderItem(17)
        item.setText(_translate("HelperDoc", "Срок обучения, лет"))
        item = self.table.horizontalHeaderItem(18)
        item.setText(_translate("HelperDoc", "Фамилия получателя"))
        item = self.table.horizontalHeaderItem(19)
        item.setText(_translate("HelperDoc", "Имя получателя"))
        item = self.table.horizontalHeaderItem(20)
        item.setText(_translate("HelperDoc", "Отчество получателя"))
        item = self.table.horizontalHeaderItem(21)
        item.setText(_translate("HelperDoc", "Дата рождения получателя "))
        item = self.table.horizontalHeaderItem(22)
        item.setText(_translate("HelperDoc", "Пол получателя"))
        item = self.table.horizontalHeaderItem(23)
        item.setText(_translate("HelperDoc", "СНИЛС"))
        item = self.table.horizontalHeaderItem(24)
        item.setText(_translate("HelperDoc", "Гражданство получателя (код страны по ОКСМ)"))
        item = self.table.horizontalHeaderItem(25)
        item.setText(_translate("HelperDoc", "Форма обучения"))
        item = self.table.horizontalHeaderItem(26)
        item.setText(_translate("HelperDoc", "Форма получения образования на момент прекращения образовательных отношений"))
        item = self.table.horizontalHeaderItem(27)
        item.setText(_translate("HelperDoc", "Источник финансирования обучения"))
        self.suggest_input_button.setText(_translate("HelperDoc", "Искать"))
        self.remove_row.setText(_translate("HelperDoc", "Удалить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelperDoc = QtWidgets.QMainWindow()
    ui = Ui_HelperDoc()
    ui.setupUi(HelperDoc)
    HelperDoc.show()
    sys.exit(app.exec())