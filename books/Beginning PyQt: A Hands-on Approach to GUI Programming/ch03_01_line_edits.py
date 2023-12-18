import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMaximumSize(350, 250)
        # self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("QLineEdit Example!")
        self.setWindowIcon(QIcon("images/heart_icon1.png"))

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        QLabel("Please enter your name:", self).move(15, 10)
        self.name_label=QLabel("Default Text ", self)
        self.name_label.move(25, 150)

        self.name_edit= QLineEdit(self)
        self.name_edit.move(15, 35)
        self.name_edit.resize(150, 20)

        # btn_clear= QPushButton("Clear", self)  ## self as an argument, sets the parent-child relationship
        self.btn_clear=QPushButton(self)
        self.btn_clear.setText("Clear")
        self.btn_clear.move(15, 75)
        self.btn_clear.clicked.connect(self.clear_text)

        self.btn_accept=QPushButton(self)
        self.btn_accept.setText("OK")
        self.btn_accept.move(100, 75)
        self.btn_accept.clicked.connect(self.accept_name)

    def clear_text(self):   ## define slot
        self.name_edit.clear()

    def accept_name(self):  ## define slot
        self.name_label.setText(self.name_edit.text())


if __name__ == "__main__":
    app= QApplication(sys.argv)
    window=MainWindow()

    sys.exit(app.exec())
