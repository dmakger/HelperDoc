import sqlite3


class Sqliter:
    def __init__(self, name_db):
        """
        Подключение к бд
        :param name_db: имя базы данных
        """
        self.connection = sqlite3.connect(name_db)
        self.cursor = self.connection.cursor()
        self.table = str()
        self.table_profession = "profession"
        self.table_qualification = "qualification"
        self.table_education_program = "education_program"
        self.table_student = "student"
        self.table_document = "document"

    @staticmethod
    def is_valid(table):
        """
        Валидна ли таблица
        :param table: название таблицы
        :return: True - если название таблицы подходит; False - если нет
        """
        is_valid = False

        if len(table) != 0 or type(table) == str:
            new_table = "".join(table.split('_'))
            is_valid = new_table.isalnum()
        return is_valid

    def connect_table(self, table):
        """
        Функция create_table создаёт таблицу в БД
        :param table: имя таблицы
        :return: True - если подключились к таблице, False - если нет
        """

        if table is None:
            table = self.table

        is_valid = False

        with self.connection:
            is_valid = self.is_valid(table)
            if is_valid:
                self.table = table
        return is_valid

    def add_qualification(self, title: str):
        """
        Функция add добавляет данные в таблицу qualification
        :return:
        """

        is_valid = False
        try:
            with self.connection:
                self.cursor.execute(f"INSERT INTO `{self.table_qualification}` (title) VALUES (?)", (title,))
                self.save()
                is_valid = True
        except sqlite3.IntegrityError:
            print("add_qualification: Такой пользователь уже существует")

        return is_valid

    def del_qualification(self, pk):
        with self.connection:
            self.cursor.execute(f'DELETE FROM {self.table_qualification} WHERE `id` = {pk}')
            self.save()

    def add_education_program(self, title: str):
        """
        Функция add добавляет данные в таблицу education_program
        :return:
        """

        is_valid = False
        try:
            with self.connection:
                self.cursor.execute(f"INSERT INTO `{self.table_education_program}` (title) VALUES (?)", (title,))
                self.save()
                is_valid = True
        except sqlite3.IntegrityError:
            print("add_education_program: Такой пользователь уже существует")

        return is_valid

    def del_education_program(self, pk):
        with self.connection:
            self.cursor.execute(f'DELETE FROM {self.table_education_program} WHERE `code` = {pk}')
            self.save()

    def add_profession(self, code: str, title: str):
        """
        Функция add добавляет данные в таблицу profession
        :return:
        """

        is_valid = False
        try:
            with self.connection:
                self.cursor.execute(f"INSERT INTO `{self.table_profession}` (code, title) VALUES (?,?)", (code, title))
                self.save()
                is_valid = True
        except sqlite3.IntegrityError:
            print("add_profession: Такой пользователь уже существует")

        return is_valid

    def del_profession(self, pk):
        with self.connection:
            self.cursor.execute(f'DELETE FROM {self.table_profession} WHERE `code` = {pk}')
            self.save()

    def add_student(self, name, last_name, middle_name, birth_date, gender,
                    snills, country_code, education_form, education_receipt_form,
                    financing_source, profession_code, qualification_id, education_program_id
                    ):
        """
        Функция add добавляет данные в таблицу student
        :return:
        """

        is_valid = False
        try:
            with self.connection:
                self.cursor.execute(f"INSERT INTO `{self.table_student}` (name, last_name, middle_name, birth_date, \
                gender, snills, country_code, education_form, education_receipt_form, financing_source, \
                profession_code, qualification_id, education_program_id) \
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (name, last_name, middle_name, birth_date, gender,
                                                          snills, country_code, education_form, education_receipt_form,
                                                          financing_source, profession_code, qualification_id,
                                                          education_program_id))
                self.save()
                is_valid = True
        except sqlite3.IntegrityError:
            print("add_student: Такой пользователь уже существует")

        return is_valid

    def del_student(self, pk):
        with self.connection:
            self.cursor.execute(f'DELETE FROM {self.table_student} WHERE `id` = {pk}')
            self.save()

    def add_document(self, title, type, series, number, loss_confirmation, exchange_confirmation,
                     destruction_confirmation, education_level, issue_date, registration_number,
                     status, student_id):
        """
        Функция add добавляет данные в таблицу profession
        :return:
        """

        is_valid = False
        try:
            with self.connection:
                self.cursor.execute(f"INSERT INTO `{self.table_document}` (title, type, series, number, \
                loss_confirmation, exchange_confirmation, destruction_confirmation, education_level, issue_date, \
                registration_number,status, student_id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (title, type, series, number,
                                                                                            loss_confirmation,
                                                                                            exchange_confirmation,
                                                                                            destruction_confirmation,
                                                                                            education_level,
                                                                                            issue_date,
                                                                                            registration_number,
                                                                                            status, student_id))
                self.save()
                is_valid = True
        except sqlite3.IntegrityError:
            print("add_document: Такой пользователь уже существует")

        return is_valid

    def del_document(self, pk):
        with self.connection:
            self.cursor.execute(f'DELETE FROM {self.table_document} WHERE `id` = {pk}')
            self.save()

    def get_last_id(self, table, name_pk):
        """
        Вернет последнее id записи из таблицы которую вы передадите
        :return:
        """

        try:
            with self.connection:
                return self.cursor.execute(f"SELECT MAX({name_pk}) FROM {table}").fetchall()[0][0]
        except sqlite3.IntegrityError:
            return -1

    def get_profession_id(self, title):
        """
        Вернет id записи из таблицы profession
        :return:
        """

        try:
            with self.connection:
                data = self.cursor.execute(
                    f'SELECT `code` FROM {self.table_profession} WHERE `title` = \'{title}\'').fetchall()
                if len(data) != 0:
                    return data[0][0]
                return -1
        except sqlite3.IntegrityError:
            return -1

    def get_profession_id_else_add(self, code, title):
        """
        Вернет id студента от таблицы profession.
        Если такого profession не существовало, то добавляет и вернет id от profession
        :return:
        """

        try:
            profession_id = self.get_profession_id(title)
            if profession_id == -1:
                self.add_profession(code, title)
                profession_id = self.get_profession_id(title)
            return profession_id
        except sqlite3.IntegrityError:
            return -1

    def get_qualification_id(self, title):
        """
        Вернет id записи от таблицы qualification.
        :return:
        """

        try:
            with self.connection:
                data = self.cursor.execute(
                    f'SELECT `code` FROM {self.table_qualification} WHERE `title` = \'{title}\'').fetchall()
                if len(data) != 0:
                    return data[0][0]
                return -1
        except sqlite3.IntegrityError:
            return -1

    def get_qualification_id_else_add(self, title):
        """
        Вернет id студента от таблицы qualification.
        Если такого qualification не существовало, то добавляет и вернет id от qualification
        :return:
        """

        try:
            qualification_id = self.get_qualification_id(title)
            if qualification_id == -1:
                self.add_qualification(title)
                qualification_id = self.get_qualification_id(title)
            return qualification_id
        except sqlite3.IntegrityError:
            return -1

    def get_education_program_id(self, title):
        """
        Вернет id записи от таблицы student.
        :return:
        """

        try:
            with self.connection:
                data = self.cursor.execute(
                    f'SELECT `code` FROM {self.table_education_program} WHERE `title` = \'{title}\'').fetchall()
                if len(data) != 0:
                    return data[0][0]
                return -1
        except sqlite3.IntegrityError:
            return -1

    def get_education_program_id_else_add(self, title):
        """
        Вернет id студента от таблицы education_program.
        Если такого education_program не существовало, то добавляет и вернет id от education_program
        :return:
        """

        try:
            education_program_id = self.get_education_program_id(title)
            if education_program_id == -1:
                self.add_education_program(title)
                education_program_id = self.get_education_program_id(title)
            return education_program_id
        except sqlite3.IntegrityError:
            return -1

    def get_student_id(self, name, last_name, middle_name, birth_date, snills):
        """
        Вернет id студента от таблицы student
        :return:
        """

        try:
            with self.connection:
                data = self.cursor.execute(
                    f'SELECT `code` FROM {self.table_student} WHERE `name` = \'{name}\' AND \
                    `last_name` = \'{last_name}\' AND `middle_name` = \'{middle_name}\' AND \
                    `birth_date` = \'{birth_date}\' AND `snills` = \'{snills}\'').fetchall()
                if len(data) != 0:
                    return data[0][0]
                return -1
        except sqlite3.IntegrityError:
            return -1

    def get_student_id_else_add(self, name, last_name, middle_name, birth_date, gender,
                                snills, country_code, education_form, education_receipt_form,
                                financing_source, profession_code, qualification_id, education_program_id):
        """
        Вернет id студента от таблицы student.
        Если такого студента не существовало, то добавляет и вернет id student
        :return:
        """

        try:
            data = [name, last_name, middle_name, birth_date, gender,
                    snills, country_code, education_form, education_receipt_form,
                    financing_source, profession_code, qualification_id, education_program_id]
            student_id = self.get_student_id(*data)
            if student_id == -1:
                self.add_student(*data)
                student_id = self.get_student_id(*data)
            return student_id
        except sqlite3.IntegrityError:
            return -1

    def get_document_id(self, title, type, series, number, loss_confirmation, exchange_confirmation,
                       destruction_confirmation, education_level, issue_date, registration_number,
                       status, student_id):
        """
        Вернет id студента от таблицы student
        :return:
        """

        try:
            with self.connection:
                data = self.cursor.execute(
                    f'SELECT `code` FROM {self.table_student} WHERE \
                    `title` = \'{title}\' AND `type` = \'{type}\' AND `series` = \'{series}\' AND \
                    `number` = \'{number}\' AND `loss_confirmation` = \'{loss_confirmation}\' AND \
                    `exchange_confirmation` = \'{exchange_confirmation}\' AND \
                    `destruction_confirmation` = \'{destruction_confirmation}\' AND \
                    `education_level` = \'{education_level}\' AND  `issue_date` = \'{issue_date}\' AND \
                    `registration_number` = \'{registration_number}\' AND `status` = \'{status}\' AND \
                    `student_id` = \'{student_id}\'').fetchall()
                if len(data) != 0:
                    return data[0][0]
                return -1
        except sqlite3.IntegrityError:
            return -1

    def get_document_id_else_add(self, name, last_name, middle_name, birth_date, gender,
                                snills, country_code, education_form, education_receipt_form,
                                financing_source, profession_code, qualification_id, education_program_id):
        """
        Вернет id студента от таблицы student.
        Если такого студента не существовало, то добавляет и вернет id student
        :return:
        """

        try:
            data = [name, last_name, middle_name, birth_date, gender,
                    snills, country_code, education_form, education_receipt_form,
                    financing_source, profession_code, qualification_id, education_program_id]
            document_id = self.get_document_id(*data)
            if document_id == -1:
                self.add_document(*data)
                document_id = self.get_document_id(*data)
            return document_id
        except sqlite3.IntegrityError:
            return -1

    # Функция save сохраняет изменения в БД
    def save(self):
        self.connection.commit()
        print(f"{self.cursor.rowcount} отредактированно строк")

    # Функция close закрывает БД
    def close(self):
        self.connection.close()
