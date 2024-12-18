import sqlite3

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton

from project.database_connection import DatabaseConnection


class EditDialog(QDialog):
    def __init__(self, parent=None, callback=None):
        super().__init__(parent)
        self.setWindowTitle('Update Student Data')
        self.setFixedSize(300, 200)

        self.callback = callback

        layout = QVBoxLayout()

        index = self.parent().table.currentRow()
        student_name = self.parent().table.item(index, 1).text()
        self.student_id = self.parent().table.item(index, 0).text()

        self.name_input = QLineEdit(student_name)
        self.name_input.setPlaceholderText('Name:')
        layout.addWidget(self.name_input)

        def_course_name = self.parent().table.item(index, 2).text()
        self.course_name = QComboBox()
        courses = ['Math', 'Science', 'History', 'Computer Science']
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(def_course_name)
        layout.addWidget(self.course_name)
        self.setLayout(layout)

        mobile = self.parent().table.item(index, 3).text()
        self.mobile = QLineEdit(mobile)
        self.mobile.setPlaceholderText('Mobile:')
        layout.addWidget(self.mobile)

        button = QPushButton('Update')
        button.clicked.connect(self.update_student)

        layout.addWidget(button)

        self.setLayout(layout)

    def update_student(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name=?, course=?, mobile=? WHERE id=?",
                       (self.name_input.text(),
                        self.course_name.itemText(self.course_name.currentIndex()),
                        self.mobile.text(),
                        self.student_id))
        connection.commit()
        cursor.close()
        connection.close()

        self.parent().load_data()

        if self.callback:
            self.callback()
        self.accept()
