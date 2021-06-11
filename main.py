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
            for i in range(self.ui.table.columnCount()):
                self.ui.table.setItem(table_row, i, QtWidgets.QTableWidgetItem(str(data[i])))
            table_row += 1

    def add_row(self):
        current_row = self.ui.table.currentRow()
        self.ui.table.insertRow(current_row+1)
        # self.mbox("Пам парам")
        # self.helper.create_row(1)

    def remove_row(self):
        if self.ui.table.rowCount() > 0:
            current_row = self.ui.table.currentRow()
            row = list()
            for col in range(self.ui.table.columnCount()):
                row.append(self.ui.table.item(current_row, col).text())
            print(row)
            result = list()
            result.append(self.helper.del_document_bd(row))
            result.append(self.helper.del_student_bd(row))
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
