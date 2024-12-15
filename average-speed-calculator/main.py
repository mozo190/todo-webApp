import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QLineEdit, QComboBox


class AvgSpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Average Speed Calculator')
        self.setStyleSheet('font-size: 20px; font-weight: bold; background-color: lightblue;')
        grid = QGridLayout()

        distance_label = QLabel('Distance:')
        self.distance_line_edit = QLineEdit()

        self.metric_combo_box = QComboBox()
        self.metric_combo_box.addItems(['Metric (km)', 'Imperial (miles)'])

        time_label = QLabel('Time (hours)')
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton('Calculate')

        avg_speed_label = QLabel('Average Speed:')

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.metric_combo_box, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 3)
        grid.addWidget(avg_speed_label, 3, 0, 1, 3)

        self.setLayout(grid)


app = QApplication(sys.argv)
avg_speed_calculator = AvgSpeedCalculator()
avg_speed_calculator.show()
sys.exit(app.exec())
