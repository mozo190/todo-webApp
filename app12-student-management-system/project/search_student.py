# This file contains the SearchStudent class which is a
# QDialog that allows the user to search for a student in the database.

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLineEdit, QPushButton)

from project.database_connection import DatabaseConnection


class SearchStudent(QDialog):
    def __init__(self, parent=None, table=None):
        super().__init__(parent)
        self.table = table
        self.setWindowTitle('Search Student')
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText('Enter student name:')
        layout.addWidget(self.search_input)

        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.perform_search)
        layout.addWidget(self.search_button)

        self.setLayout(layout)

    def perform_search(self):
        try:
            search_term = self.search_input.text()
            with DatabaseConnection().connect() as connect:
                with connect.cursor() as cursor:
                    cursor.execute('SELECT * FROM students WHERE name LIKE %s', (f'{search_term}%',))
                    results = cursor.fetchall()

                    if not results:
                        print('Student not found')
                        return

            student = self.table.findItems(search_term, Qt.MatchFlag.MatchContains)

            if not student:
                print('Student not found in table')
                return

            for item in student:
                print(item.row(), item.column())
                self.table.item(item.row(), item.column()).setBackground(Qt.GlobalColor.red)

            cursor.close()
            connect.close()

            if student:
                print(student)

        except Exception as ex:
            print(f'Error searching student {ex}')
