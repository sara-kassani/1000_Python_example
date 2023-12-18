import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(450, 350)
        self.setWindowTitle("Main Window Template")
        self.setWindowIcon(QIcon("images/heart_icon1.png"))

        self.setUpMainWindow()
        self.createAction()
        self.createMenu()
        self.show()


    def setUpMainWindow(self):
        pass

    def createAction(self):
        self.quit_act=QAction(" Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

    def createMenu(self):
        self.menuBar().setNativeMenuBar(False)

        ## create file menu and add actions
        file_menu= self.menuBar().addMenu("File")
        file_menu.addAction(self.quit_act)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    sys.exit(app.exec())

