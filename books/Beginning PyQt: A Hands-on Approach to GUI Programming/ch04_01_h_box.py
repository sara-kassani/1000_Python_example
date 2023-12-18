import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PyQt6.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumWidth(500)
        self.setFixedHeight(60)
        self.setWindowTitle("QHBoxLayout Example")
        self.setWindowIcon(QIcon("images/heart_icon1.png"))

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.name_label= QLabel("New Username: ", self)
        self.name_edit= QLineEdit(self)
        self.name_edit.setClearButtonEnabled(True)
        self.name_edit.textEdited.connect(self.check_user_input)

        self.confirm_button=QPushButton("Confirm", self)
        self.confirm_button.setEnabled(False)
        self.confirm_button.clicked.connect(self.close)

        h_box=QHBoxLayout()
        h_box.addWidget(self.name_label)
        h_box.addWidget(self.name_edit)
        h_box.addWidget(self.confirm_button)

        self.setLayout(h_box)


    def check_user_input(self, text):
        if len(text) > 0 and all(t.isalpha() or t.isdigit() for t in text):
            self.confirm_button.setEnabled(True)
        else:
            self.confirm_button.setEnabled(False)

if __name__ == "__main__":
    app= QApplication(sys.argv)
    window= MainWindow()

    sys.exit(app.exec())