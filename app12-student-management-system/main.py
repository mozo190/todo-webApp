import sqlite3
import sys

from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QToolBar, QStatusBar,
                             QPushButton)

from project.insert_dialog import InsertDialog
from project.edit_dialog import EditDialog
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
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)
        toolbar.addAction(exit_action)

        self.statusbar = QStatusBar()
        self.statusbar().setStatusBar(self.statusbar)

        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        edit_button = QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.delete_record)

        children = self.statusBar().findChildren(QPushButton)
        if children:
            for child in children:
                self.statusBar().removeWidget(child)

        self.statusBar().addWidget(edit_button)
        self.statusBar().addWidget(delete_button)

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
        dialog = InsertDialog(callback=self.load_data, parent=self)
        dialog.exec()

    def edit(self):
        dialog = EditDialog(parent=self, callback=self.load_data)
        dialog.exec()

    def delete_record(self):
        index = self.table.currentRow()
        if index >= 0:
            student_id = self.table.item(index, 0).text()
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            cursor.execute('DELETE FROM students WHERE id=?', (student_id,))
            connection.commit()
            cursor.close()
            connection.close()
            self.load_data()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.load_data()
    sys.exit(app.exec())
