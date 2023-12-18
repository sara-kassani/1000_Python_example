import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout
from PyQt6.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(300, 200)
        self.setWindowTitle("Spacing Example")

        self.setUpMainWIndow()
        self.show()

    def setUpMainWIndow(self):
        label=QLabel("Enter text")
        line_edit=QLineEdit()
        button=QPushButton("End")
        button.clicked.connect(self.close)

        main_v_box=QVBoxLayout()
        main_v_box.addWidget(label)
        main_v_box.addSpacing(10)
        main_v_box.addWidget(line_edit)
        main_v_box.addStretch()
        main_v_box.addWidget(button)

        self.setLayout(main_v_box)


if __name__ == "__main__":
    app= QApplication(sys.argv)
    window=MainWindow()

    sys.exit(app.exec())