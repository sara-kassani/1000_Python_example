import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("QPushButton Example")
        self.setWindowIcon(QIcon("images/heart_icon1.png"))

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.btn1= QPushButton(self)
        self.btn1.setText("Push me")
        self.btn1.move(30, 20)
        self.btn1.clicked.connect(self.btnClicked)

        self.lbl1=QLabel("Don't push the button", self)
        self.lbl1.move(30, 80)
        
    def btnClicked(self):
        self.lbl1.setText("Clicked!")


if __name__ == "__main__":
    app=QApplication(sys.argv)
    window= MainWindow()

    sys.exit(app.exec())