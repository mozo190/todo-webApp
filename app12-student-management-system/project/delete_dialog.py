import sqlite3

from PyQt6.QtWidgets import QDialog, QGridLayout, QLabel, QPushButton


class DeleteDialog(QDialog):
    def __init__(self, parent=None, callback=None):
        super().__init__(parent)
        self.setWindowTitle('Update Student Data')

        self.callback = callback

        layout = QGridLayout()
        confirmation = QLabel('Are you sure you want to delete this student?')
        yes = QPushButton('Yes')
        no = QPushButton('No')

        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)
        self.setLayout(layout)

        yes.clicked.connect(self.delete_student)

        no.clicked.connect(self.reject)

    def delete_student(self):
        index = self.parent().table.currentRow()
        student_id = self.parent().table.item(index, 0).text()

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
        connection.commit()
        cursor.close()
        connection.close()

        self.parent().load_data()

        if self.callback:
            self.callback()
        self.accept()
