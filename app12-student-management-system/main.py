import sqlite3
import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QLineEdit,
                             QComboBox, QPushButton)


class InsertDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Add Student')
        self.setFixedSize(300, 200)

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
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute('INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)',
                       (name, course, mobile))
        connect.commit()
        cursor.close()
        connect.close()

        main_window.load_data()
        self.accept()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')
        self.setGeometry(100, 100, 800, 600)

        file_menu_item = self.menuBar().addMenu('File')
        help_menu_item = self.menuBar().addMenu('Help')
        search_menu_item = self.menuBar().addMenu('Search')

        add_student_action = QAction('Add Student', self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(QApplication.instance().quit)
        file_menu_item.addAction(exit_action)

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

    def insert(self):
        dialog = InsertDialog(self)
        dialog.exec()


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())
