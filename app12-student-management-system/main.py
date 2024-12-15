import sqlite3
import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QLineEdit,
                             QComboBox)


class InsertDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Add Student')
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText('Name:')
        layout.addWidget(self.name_input)

        course_name = QComboBox()
        courses = ['Math', 'Science', 'History', 'Computer Science']
        course_name.addItems(courses)
        layout.addWidget(course_name)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')
        self.setGeometry(100, 100, 800, 600)

        file_menu_item = self.menuBar().addMenu('File')
        help_menu_item = self.menuBar().addMenu('Help')

        add_student_action = QAction('Add Student', self)
        add_student_action.triggered.connect(self.add_student)
        file_menu_item.addAction(add_student_action)

        about_action = QAction('About', self)
        help_menu_item.addAction(about_action)

        about_action.setMenuRole(QAction.MenuRole.NoRole)

        self.table = QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(4)

        self.table.setHorizontalHeaderLabels(('ID', 'Name', 'Course', 'Mobile'))
        self.table.setStyleSheet('font-weight: bold')
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect('database.db')
        result = connection.execute('SELECT * FROM students')
        data_ = list(result)
        self.table.setRowCount(len(data_))
        for row_number, row_data in enumerate(data_):
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def add_student(self):
        dialog = InsertDialog(self)
        dialog.exec()


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())