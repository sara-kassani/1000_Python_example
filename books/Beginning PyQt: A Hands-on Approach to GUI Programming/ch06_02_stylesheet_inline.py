import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout)

class MainWinddow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(200, 200)
        self.setWindowTitle("Style SHeet Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        label=QLabel("<p align=center> Give me a like! </p>", self)
        label.setStyleSheet("""
                            background-color: skyblue;
                            color: white;
                            border-style: outset;
                            border-width: 3px;
                            border-radius: 5px;
                            font: bold 24px 'Times New Roman' """)

        like_btn=QPushButton()
        like_btn.setStyleSheet(""" QPushButton {
            background-color: lightgrey; 
            padding: 5px;
            border-style: inset;
            border-width: 1px;  
            border-radius: 5px;             
            image: url(images/flower_icon1.png);
            qproperty-iconSize: 20px 20px;}

            QPushButton:pressed {background-color: red;
                    padding: 5px;
                    border-style: outset; 
                    border-width: 1px; 
                    border-radius: 5px;
                    image: url(images/flower_icon2.png);
                    qproperty-iconSize: 20px 20px;}""")


        v_box=QVBoxLayout()
        v_box.addWidget(label)
        v_box.addWidget(like_btn)
        
        self.setLayout(v_box)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWinddow()

    sys.exit(app.exec())