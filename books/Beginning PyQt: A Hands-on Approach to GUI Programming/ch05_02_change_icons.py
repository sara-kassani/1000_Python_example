import sys, random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(200, 200)
        self.setWindowTitle("Changing Icon Example")
        self.setWindowIcon(QIcon("images/heart_icon1.png"))

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.info_lbl=QLabel("Click on the button and select an animal.", self)
        self.info_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.images=["images\cute_rabbit1.jpg",
                     "images\cute_dog6.jpg",
                     "images\cute_peacock.png",
                     "images\cute_rabbit1.jpg"]
        
        self.icon_button=QPushButton()
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(100, 100))
        self.icon_button.clicked.connect(self.change_button_icon)


    ## create vertical layout and add widgets
        main_vbox=QVBoxLayout()
        main_vbox.addWidget(self.info_lbl)
        main_vbox.addWidget(self.icon_button)

    ## set main layout of window
        container=QWidget()
        container.setLayout(main_vbox)
        self.setCentralWidget(container)

    def change_button_icon(self):
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(100, 100))
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()

    sys.exit(app.exec())