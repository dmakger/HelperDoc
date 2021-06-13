import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox

from design import Ui_HelperDoc
from excel import Excel
from helper import Helper


class HelperDoc(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.excel = Excel("ККМТ2020 Очно.xlsx")
        self.helper = Helper('db.db')
        self.excel.max_col = 28
        self.excel.max_row = 11

        self.ui = Ui_HelperDoc()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('HelperDoc')
        self.setWindowIcon(QIcon('favicon.ico'))

        self.ui.suggest_input.setPlaceholderText('Поиск...')
        self.load_data()
        self.ui.clear.clicked.connect(lambda: self.clear_data())
        self.ui.add_row.clicked.connect(lambda: self.add_row())
        self.ui.table.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        self.ui.remove_row.clicked.connect(lambda: self.remove_row())

    def load_data(self):
        # [(1,), (2,), (3,)]
        all_id = self.helper.bd.select(self.helper.table_document, 'id', {})
        # [1, 2, 3]
        all_id = [pk[0] for pk in all_id]

        table_row = 0
        self.ui.table.setRowCount(len(all_id))
        for pk in all_id:
            data = self.helper.create_row(pk)
            for i in range(self.ui.table.columnCount()):
                self.ui.table.setItem(table_row, i, QtWidgets.QTableWidgetItem(str(data[i])))
            table_row += 1

    def get_row_by_position(self, position):
        row = list()
        for col in range(self.ui.table.columnCount()):
            row.append(self.ui.table.item(position, col).text())
        return row

    def add_row_excel(self):
        current_row_position = self.ui.table.currentRow()
        # current_row_position = 0
        # # row = self.get_row_by_position(current_row_position)
        # row = self.excel.get_row(20)
        # result = list()
        # result.append(self.helper.add_all_bd(row))
        # print(result)
        self.ui.table.insertRow(current_row_position + 1)
        # self.mbox("Пам парам")
        # self.helper.create_row(1)

    def clear_data(self):
        self.ui.title_doc_line.clear()
        self.ui.type_doc_line.clear()
        self.ui.status_doc_line.clear()
        self.ui.loss_confirmation_line.clear()
        self.ui.confirmation_exchange_line.clear()
        self.ui.destruction_confirmation_line.clear()
        self.ui.education_level_line.clear()
        self.ui.series_doc_line.clear()
        self.ui.number_doc_line.clear()
        self.ui.issue_date_line.clear()
        self.ui.registration_number_line.clear()
        self.ui.code_profession_line.clear()
        self.ui.title_profession_line.clear()
        self.ui.education_program_line.clear()
        self.ui.admission_year_line.clear()
        self.ui.graduation_year_line.clear()
        self.ui.study_period_line.clear()
        self.ui.last_name_line.clear()
        self.ui.name_line.clear()
        self.ui.middle_name_line.clear()
        self.ui.birth_date_line.clear()
        self.ui.gender_line.clear()
        self.ui.snills_line.clear()
        self.ui.country_code_line.clear()
        self.ui.education_form_line.clear()
        self.ui.education_receipt_form_line.clear()
        self.ui.financing_source_line.clear()

    def get_inputted_data(self):
        data = list()
        data.append(self.ui.title_doc_line.text())
        data.append(self.ui.type_doc_line.text())
        data.append(self.ui.status_doc_line.text())
        data.append(self.ui.loss_confirmation_line.text())
        data.append(self.ui.confirmation_exchange_line.text())
        data.append(self.ui.destruction_confirmation_line.text())
        data.append(self.ui.education_level_line.text())
        data.append(self.ui.series_doc_line.text())
        data.append(self.ui.number_doc_line.text())
        data.append(self.ui.issue_date_line.text())
        data.append(self.ui.registration_number_line.text())
        data.append(self.ui.code_profession_line.text())
        data.append(self.ui.title_profession_line.text())
        data.append(self.ui.education_program_line.text())
        data.append(self.ui.admission_year_line.text())
        data.append(self.ui.graduation_year_line.text())
        data.append(self.ui.study_period_line.text())
        data.append(self.ui.last_name_line.text())
        data.append(self.ui.name_line.text())
        data.append(self.ui.middle_name_line.text())
        data.append(self.ui.birth_date_line.text())
        data.append(self.ui.gender_line.text())
        data.append(self.ui.snills_line.text())
        data.append(self.ui.country_code_line.text())
        data.append(self.ui.education_form_line.text())
        data.append(self.ui.education_receipt_form_line.text())
        data.append(self.ui.financing_source_line.text())
        return data

    def add_row(self):
        new_row_position = self.ui.table.currentRow() + 1
        self.ui.table.insertRow(new_row_position)
        inputted_data = self.get_inputted_data()
        print(inputted_data)
        for i in range(len(inputted_data)):
            self.ui.table.setItem(new_row_position, i, QtWidgets.QTableWidgetItem(inputted_data[i]))
        try:
            print(len(inputted_data))
            self.helper.add_all_bd(inputted_data)
            for i in range(len(inputted_data)):
                self.ui.table.setItem(new_row_position, i, QtWidgets.QTableWidgetItem(inputted_data[i]))
        except Exception:
            self.mbox("Некоректный ввод данных")

    def remove_row(self):
        if self.ui.table.rowCount() > 0:
            current_row_position = self.ui.table.currentRow()
            print(current_row_position)
            row = self.get_row_by_position(current_row_position)

            result = list()
            result.append(self.helper.del_all_bd(row))
            print(result)
            self.ui.table.removeRow(current_row_position)
        else:
            self.mbox("Невозможно удалить, так как таблица пуста")

    def mbox(self, body, title='Ошибка'):
        dialog = QMessageBox()
        dialog.setText(body)
        dialog.setWindowTitle(title)
        dialog.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        dialog.exec()


app = QtWidgets.QApplication([])
application = HelperDoc()
application.show()

sys.exit(app.exec())
