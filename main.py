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

        # rows = self.excel.get_rows(False)
        # print(rows[0])

        # first_row = rows[0]

        self.ui = Ui_HelperDoc()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('HelperDoc')
        self.setWindowIcon(QIcon('favicon.ico'))

        self.ui.suggest_input.setPlaceholderText('Поиск...')
        self.load_data()
        self.ui.add_row.clicked.connect(lambda: self.add_row())
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
            print(data)
            for i in range(self.ui.table.columnCount()):
                self.ui.table.setItem(table_row, i, QtWidgets.QTableWidgetItem(str(data[i])))
            table_row += 1

    def get_row_by_position(self, position):
        row = list()
        for col in range(self.ui.table.columnCount()):
            row.append(self.ui.table.item(position, col).text())
        print(row)
        return row

    def add_row(self):
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

    def remove_row(self):
        if self.ui.table.rowCount() > 0:
            print("qwe")
            current_row = self.ui.table.currentRow()
            row = self.get_current_row(current_row)
            result = list()
            result.append(self.helper.del_all_bd(row))
            print(result)
            self.ui.table.removeRow(current_row)

    def mbox(self, body, title='Bruh'):
        dialog = QMessageBox()
        dialog.setText(body)
        dialog.setWindowTitle(title)
        dialog.exec()


app = QtWidgets.QApplication([])
application = HelperDoc()
application.show()

sys.exit(app.exec())
