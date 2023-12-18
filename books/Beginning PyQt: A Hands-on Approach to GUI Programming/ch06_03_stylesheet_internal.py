import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


style_sheet = """
    QPushButton#Warning_Button{
        background-color: #C92108;
        border-radius: 5px;
        padding: 6px;
        color: #FFFFFF
    }
    QPushButton#Warning_Button:pressed{
        background-color: #F4B519;
    }
"""

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(250, 150)
        self.setWindowTitle("CSS Internal")

        label=QLabel("Push a button")

        normal_btn=QPushButton("Normal")
        warning_btn=QPushButton("Warning!")
        warning_btn.setObjectName("Warning_Button")  ## set ID selector

        v_box=QVBoxLayout()
        v_box.addWidget(label)
        v_box.addWidget(normal_btn)
        v_box.addWidget(warning_btn)

        self.setLayout(v_box)
        self.show()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    app.setStyleSheet(style_sheet)

    window=MainWindow()
    sys.exit(app.exec())