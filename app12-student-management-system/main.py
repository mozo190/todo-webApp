import logging
import sys

import mysql
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QToolBar, QStatusBar,
                             QPushButton, QScrollArea)

from project.about_dialog import AboutDialog
from project.database_connection import DatabaseConnection
from project.delete_dialog import DeleteDialog
from project.edit_dialog import EditDialog
from project.insert_dialog import InsertDialog
from project.search_student import SearchStudent

main_window = None


def get_main_window():
    global main_window
    return main_window


logging.basicConfig(
    level=logging.DEBUG,
    filename="error.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def initialize_database():
    connection = DatabaseConnection().connect()
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS students ('
                   'id INT AUTO_INCREMENT PRIMARY KEY, '
                   'name VARCHAR(255), '
                   'course VARCHAR(255), '
                   'mobile VARCHAR(255))'
                   )
    connection.commit()
    cursor.close()
    connection.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')
        self.setGeometry(100, 100, 800, 600)

        file_menu_item = self.menuBar().addMenu('File')
        edit_menu_item = self.menuBar().addMenu('Edit')
        help_menu_item = self.menuBar().addMenu('Help')

        add_student_action = QAction(QIcon("icons/add.png"), 'Add Student', self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        search_action = QAction(QIcon('icons/search.png'), 'Search', self)
        edit_menu_item.addAction(search_action)
        search_action.triggered.connect(self.search_student)

        exit_action = QAction(QIcon('icons/exit.png'), 'Exit', self)
        exit_action.triggered.connect(QApplication.instance().quit)
        file_menu_item.addAction(exit_action)

        about_action = QAction('About', self)
        help_menu_item.addAction(about_action)

        about_action.setMenuRole(QAction.MenuRole.NoRole)
        about_action.triggered.connect(self.about)

        self.table = QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(4)

        self.table.setHorizontalHeaderLabels(('ID', 'Name', 'Course', 'Mobile'))
        self.table.horizontalHeader().setStyleSheet('font-weight: bold; background-color: lightgrey')
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.table)
        self.setCentralWidget(scroll_area)

        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)
        toolbar.addAction(exit_action)

        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.statusBar().setStyleSheet('background-color: lightgrey')

        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        edit_button = QPushButton("Edit Record")
        edit_button.setStyleSheet('background-color: lightblue')
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton("Delete")
        delete_button.setStyleSheet('background-color: lightcoral')
        delete_button.clicked.connect(self.delete_record)

        children = self.statusBar().findChildren(QPushButton)
        if children:
            for child in children:
                self.statusBar().removeWidget(child)

        self.statusBar().addWidget(edit_button)
        self.statusBar().addWidget(delete_button)

    def load_data(self):
        try:
            connection = DatabaseConnection().connect()
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM students')
            result = cursor.fetchall()
            data_ = list(result)
            self.table.setRowCount(len(data_))
            for row_number, row_data in enumerate(data_):
                for column_number, data in enumerate(row_data):
                    self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            cursor.close()
            connection.close()
        except mysql.connector.Error as e:
            logging.error(f'Error loading data: {e}')
            self.statusBar().showMessage('Error loading data', 5000)

    def search_student(self):
        try:
            dialog = SearchStudent(self, self.table)
            dialog.exec()
        except mysql.connector.Error as er:
            logging.error(f'Error searching student: {er}')
            self.statusBar().showMessage('Error searching student', 5000)

    def insert(self):
        try:
            dialog = InsertDialog(parent=self, callback=self.load_data)
            dialog.exec()
        except mysql.connector.Error as me:
            logging.error(f'Error inserting data: {me}')
            self.statusBar().showMessage('Error inserting data', 5000)

    def edit(self):
        try:
            dialog = EditDialog(parent=self, callback=self.load_data)
            dialog.exec()
        except mysql.connector.Error as e:
            logging.error(f'Error updating data: {e}')
            self.statusBar().showMessage('Error updating data', 5000)

    def delete_record(self):
        try:
            dialog = DeleteDialog(parent=self, callback=self.load_data)
            dialog.exec()
        except mysql.connector.Error as er:
            logging.error(f'Error deleting data: {er}')
            self.statusBar().showMessage('Error deleting data', 5000)

    def about(self):
        dialog = AboutDialog(self)
        dialog.exec()


if __name__ == '__main__':
    initialize_database()
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    try:
        main_window.load_data()
    except Exception as e:
        logging.error(f'Error loading data: {e}')
        main_window.statusBar().showMessage('Error loading data', 5000)
    sys.exit(app.exec())
