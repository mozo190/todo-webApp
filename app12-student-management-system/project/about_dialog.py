from PyQt6.QtWidgets import QMessageBox


class AboutDialog(QMessageBox):
    def __init__(self, parent=None, callback=None):
        super().__init__(parent)
        self.setWindowTitle('About')
        self.setText('This is a simple student registration application.')
        self.setInformativeText('Developed by: MoZo')
        self.setIcon(QMessageBox.Icon.Information)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)

        if callback:
            callback()
