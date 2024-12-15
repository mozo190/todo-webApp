import sqlite3

from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLineEdit, QPushButton)


class SearchStudent(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
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
        search_term = self.search_input.text()
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM students WHERE name = ?', (search_term))
        student = cursor.fetchall()

        cursor.close()
        connect.close()

