from excel import Excel
from sqlite import Sqliter


class Helper:

    def __init__(self, bd):
        self.bd = Sqliter(bd)
        self.table_profession = "profession"
        self.table_qualification = "qualification"
        self.table_education_program = "education_program"
        self.table_student = "student"
        self.table_document = "document"

    @staticmethod
    def get_profession(row, is_form_list=False):
        if is_form_list:
            return [row[11], row[12]]

        return {
            'code': row[11],
            'title': row[12]
        }

    def add_profession_bd(self, row):
        data = dict()
        if (type(row) is list) or (type(row) is tuple):
            data = self.get_profession(row)
        if type(row) is dict:
            data = row

        self.bd.get_profession_id_else_add(data['code'], data['title'])

    def del_professional_bd(self, row):
        self.bd.del_profession(self.get_profession(row, True))

    @staticmethod
    def get_qualification(row, is_form_list=False):
        if is_form_list:
            return [row[13]]
        return {
            'title': row[13]
        }

    def add_qualification_bd(self, row):
        data = dict()
        if (type(row) is list) or (type(row) is tuple):
            data = self.get_qualification(row)
        if type(row) is dict:
            data = row

        self.bd.get_qualification_id_else_add(data['title'])

    def del_qualification_bd(self, row):
        self.bd.del_qualification(self.get_qualification(row, True))

    @staticmethod
    def get_education_program(row, is_form_list=False):

        if is_form_list:
            return [row[14]]

        return {
            'title': row[14]
        }

    def add_education_program_bd(self, row):
        data = dict()
        if (type(row) is list) or (type(row) is tuple):
            data = self.get_education_program(row)
        if type(row) is dict:
            data = row

        self.bd.get_education_program_id_else_add(data['title'])

    def del_education_program_bd(self, row):
        self.bd.del_qualification(self.get_education_program(row, True))

    def get_student(self, row, is_form_list=False):
        qualification_id = self.bd.get_qualification_id(row[13])
        education_program_id = self.bd.get_education_program_id(row[14])

        if (qualification_id == -1) or (education_program_id == -1):
            return -1

        if is_form_list:
            return [
                row[19], row[18], row[20], row[21].strftime("%d.%m.%y"),
                row[22], row[23], row[24], row[25], row[26], row[27], row[11],
                qualification_id, education_program_id,
            ]

        return {
            'name': row[19],
            'last_name': row[18],
            'middle_name': row[20],
            'birth_date': row[21].strftime("%d.%m.%y"),
            'gender': row[22],
            'snills': row[23],
            'country_code': row[24],
            'education_form': row[25],
            'education_receipt_form': row[26],
            'financing_source': row[27],
            'profession_code': row[11],
            'qualification_id': qualification_id,
            'education_program_id': education_program_id,
        }

    def add_student_bd(self, row):
        data = dict()
        if (type(row) is list) or (type(row) is tuple):
            data = self.get_student(row)
        if type(row) is dict:
            data = row

        self.bd.get_student_id_else_add(
            data['name'],
            data['last_name'],
            data['middle_name'],
            data['birth_date'],
            data['gender'],
            data['snills'],
            data['country_code'],
            data['education_form'],
            data['education_receipt_form'],
            data['financing_source'],
            data['profession_code'],
            data['qualification_id'],
            data['education_program_id'],
        )

    def del_student_bd(self, row):
        self.bd.del_student(self.get_student(row, True))

    def get_document(self, row, is_form_list=False):
        student_all_data = self.get_student(row)
        student = [
            student_all_data['name'],
            student_all_data['last_name'],
            student_all_data['middle_name'],
            student_all_data['birth_date'],
            student_all_data['snills'],
        ]
        student_id = self.bd.get_student_id(*student)
        if student_id == -1:
            return -1

        if is_form_list:
            return [
                row[0], row[1], row[7], row[8], row[3],
                row[4], row[5], row[6], row[9], row[10],
                row[2], student_id,
            ]

        return {
            'title': row[0],
            'type': row[1],
            'series': row[7],
            'number': row[8],
            'loss_confirmation': row[3],
            'exchange_confirmation': row[4],
            'destruction_confirmation': row[5],
            'education_level': row[6],
            'issue_date': row[9],
            'registration_number': row[10],
            'status': row[2],
            'student_id': student_id,
        }

    def add_document_bd(self, row):
        data = dict()
        if (type(row) is list) or (type(row) is tuple):
            data = self.get_document(row)
        if type(row) is dict:
            data = row

        self.bd.get_document_id_else_add(
            data['title'],
            data['type'],
            data['series'],
            data['number'],
            data['loss_confirmation'],
            data['exchange_confirmation'],
            data['destruction_confirmation'],
            data['education_level'],
            data['issue_date'],
            data['registration_number'],
            data['status'],
            data['student_id'],
        )

    def del_document_bd(self, row):
        self.bd.del_document(self.get_document(row, True))

    def add_all_bd(self, row):
        self.add_profession_bd(self.get_profession(row))
        self.add_qualification_bd(self.get_qualification(row))
        self.add_education_program_bd(self.get_education_program(row))
        self.add_student_bd(self.get_student(row))
        self.add_document_bd(self.get_document(row))

    def del_all_bd(self, row):
        self.del_document_bd(row)
        self.add_student_bd(row)
        self.add_education_program_bd(row)
        self.add_profession_bd(row)
        self.del_professional_bd(row)


if __name__ == '__main__':
    doc = Excel("ККМТ2020 Очно.xlsx")
    doc.max_col = 28
    doc.max_row = 11

    rows = doc.get_rows(False)

    first_row = rows[1]
    title = doc.get_title_row()
    for i in range(len(title)):
        print(f"{i}| {title[i]}: {first_row[i]}")

    helper = Helper('db.db')

    # helper.add_all_bd(rows[1])
    # bd = Sqliter('db.db')
    helper.del_all_bd(rows[0])