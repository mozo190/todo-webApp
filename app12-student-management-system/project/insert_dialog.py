import sqlite3

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton

from project.database_connection import DatabaseConnection


class InsertDialog(QDialog):
    def __init__(self, parent=None, callback=None):
        super().__init__(parent)
        self.setWindowTitle('Add Student')
        self.setFixedSize(300, 200)

        self.callback = callback

        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText('Name:')
        layout.addWidget(self.name_input)

        self.course_name = QComboBox()
        courses = ['Math', 'Science', 'History', 'Computer Science']
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)
        self.setLayout(layout)

        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText('Mobile:')
        layout.addWidget(self.mobile)

        button = QPushButton('Register')
        button.clicked.connect(self.add_student)

        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.name_input.text()
        course = self.course_name.currentText()
        mobile = self.mobile.text()

        connect = DatabaseConnection().connect()
        cursor = connect.cursor()
        cursor.execute('INSERT INTO students (name, course, mobile) VALUES (%s, %s, %s)',
                       (name, course, mobile))
        connect.commit()
        cursor.close()
        connect.close()

        if self.callback:
            self.callback()
        self.accept()
