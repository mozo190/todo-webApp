import sqlite3
import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QToolBar)

from project.insert_dialog import InsertDialog
from project.search_student import SearchStudent

main_window = None


def get_main_window():
    global main_window
    return main_window


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')
        self.setGeometry(100, 100, 800, 600)

        file_menu_item = self.menuBar().addMenu('File')
        help_menu_item = self.menuBar().addMenu('Help')
        edit_menu_item = self.menuBar().addMenu('Edit')

        add_student_action = QAction('Add Student', self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        search_action = QAction('Search', self)
        edit_menu_item.addAction(search_action)
        search_action.triggered.connect(self.search_student)

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
        self.table.horizontalHeader().setStyleSheet('font-weight: bold; background-color: lightgrey')
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)

    def load_data(self):
        connection = sqlite3.connect('database.db')
        result = connection.execute('SELECT * FROM students')
        data_ = list(result)
        self.table.setRowCount(len(data_))
        for row_number, row_data in enumerate(data_):
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def search_student(self):
        dialog = SearchStudent(self, self.table)
        dialog.exec()

    def insert(self):
        dialog = InsertDialog(callback=self.load_data)
        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.load_data()
    sys.exit(app.exec())
