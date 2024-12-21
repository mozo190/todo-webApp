from PyQt6.QtWidgets import QDialog, QGridLayout, QLabel, QPushButton, QMessageBox

from project.database_connection import DatabaseConnection


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
        # Check if a student is selected
        if index == -1:
            QMessageBox().warning(self, 'No Student Selected', 'Please select a student to delete.')
            return

        student_id = self.parent().table.item(index, 3).text()

        if not student_id:
            QMessageBox().warning(self, 'No Student Selected', 'Please select a student to delete.')
            return

        try:
            connection = DatabaseConnection().connect()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
            connection.commit()
            cursor.close()
            connection.close()

            self.parent().load_data()

            self.close()

            confirmation_widget = QMessageBox()
            confirmation_widget.setWindowTitle('Student Deleted')
            confirmation_widget.setText('Student has been deleted successfully.')
            confirmation_widget.exec()

            if self.callback:
                self.callback()
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, 'Error Deleting Student', f'Error deleting student: {e}')
