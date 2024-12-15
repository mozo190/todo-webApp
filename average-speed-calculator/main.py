import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QComboBox


class AvgSpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Average Speed Calculator')
        self.setStyleSheet('font-size: 20px; font-weight: bold; background-color: orange;')
        grid = QGridLayout()

        distance_label = QLabel('Distance:')
        self.distance_line_edit = QLineEdit()
        self.distance_line_edit.setStyleSheet('background-color: white;')

        self.metric_combo_box = QComboBox()
        self.metric_combo_box.addItems(['Metric (km)', 'Imperial (miles)'])
        self.metric_combo_box.setStyleSheet('background-color: white;')

        time_label = QLabel('Time (hours)')
        self.time_line_edit = QLineEdit()
        self.time_line_edit.setStyleSheet('background-color: white;')

        calculate_button = QPushButton('Calculate')
        calculate_button.setStyleSheet('background-color: brown; color: white;')

        self.avg_speed_label = QLabel('Average Speed:')
        self.avg_speed_label.setStyleSheet('font-size: 30px; font-weight: bold; color: red;')

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.metric_combo_box, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 3)
        grid.addWidget(self.avg_speed_label, 3, 0, 1, 3)

        calculate_button.clicked.connect(self.calculate_speed)
        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())
        if self.metric_combo_box.currentText() == 'Metric (km)':
            speed = round(distance / time, 2)
            self.avg_speed_label.setText(f'Average Speed: {speed} km/h')
        else:
            speed = round(distance / time * 0.621371, 2)
            self.avg_speed_label.setText(f'Average Speed: {speed} miles/h')


app = QApplication(sys.argv)
avg_speed_calculator = AvgSpeedCalculator()
avg_speed_calculator.show()
sys.exit(app.exec())
