import sys
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Event Handling Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        info_lbl=QLabel("Press the <b>Escape </b> to close the window")

        self.setCentralWidget(info_lbl)   ## setCentralWidget is available in QMainWindow

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            print("Application closed.")
            self.close()


if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()

    sys.exit(app.exec())

