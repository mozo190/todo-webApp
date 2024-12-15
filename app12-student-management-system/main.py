import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')
        self.setGeometry(100, 100, 800, 600)

        file_menu_item = self.menuBar().addMenu('File')
        help_menu_item = self.menuBar().addMenu('Help')

        add_student_action = QAction('Add Student', self)
        file_menu_item.addAction(add_student_action)

        about_action = QAction('About', self)
        help_menu_item.addAction(about_action)

        about_action.setMenuRole(QAction.MenuRole.NoRole)

        self.table = QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(4)

        self.table.setHorizontalHeaderLabels(('ID', 'Name', 'Course', 'Mobile'))
        self.table.setStyleSheet('font-size: 20px, font-family: Arial, font-weight: bold')
        self.setCentralWidget(self.table)

    def load_data(self):
        pass


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
