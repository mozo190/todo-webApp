class EditDialog(QDialog):
  def __init__(self, parent=None, callback=None):
        super().__init__(parent)
        self.setWindowTitle('Update Student Data')
        self.setFixedSize(300, 200)

        self.callback = callback

        layout = QVBoxLayout()

        index = main_window.table.currentRow()
        student_name = main.window.table.item(index, 1).text()
    
        self.name_input = QLineEdit(student_name)
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
        button.clicked.connect(self.update_student)

        layout.addWidget(button)

        self.setLayout(layout)
    
  def update_student(self):
        pass    
