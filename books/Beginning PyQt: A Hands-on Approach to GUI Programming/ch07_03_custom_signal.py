import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal, QObject

class SendSignal(QObject):
    change_style=pyqtSignal()

class MainWinddow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 200, 300, 200)
        self.setWindowTitle("Custon Signal Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.index= 0  ## Index of items in list
        self.direction=""

        ## create instance of SendSignal class and 
        ## connect change_style signal to a slot

        self.sig=SendSignal()
        self.sig.change_style.connect(self.change_background)

        header_lbl=QLabel(
            """ <p align='center'> Press the <b> up </b> and <b> down </b> arrows. </p> """)
        
        self.color_list=["red", "orange", "yellow", "green", "blue", "purple"]
        
        self.label=QLabel()
        self.setStyleSheet(f"""background-color:{self.color_list[self.index]}""")

        main_v_box=QVBoxLayout()
        main_v_box.addWidget(header_lbl)
        main_v_box.addWidget(self.label)

        container=QWidget()
        container.setLayout(main_v_box)
        self.setCentralWidget(container)

    def keyPressEvent(self, event):
        """Reimplement how the key press event is handled"""
        if event.key() == Qt.Key.Key_Up:
            self.direction="up"
            self.sig.change_style.emit()

        elif event.key() == Qt.Key.Key_Down:
            self.direction="down"
            self.sig.change_style.emit()

    def change_background(self):
        """change the background of the label widget when 
        a keyPressEvent signal is emitted."""
        if self.direction=="up" and self.index <len(self.color_list) -1:
            self.index=self.index+1
            self.label.setStyleSheet(f"""background-color:{self.color_list[self.index]}""")
        elif self.direction == "down" and self.index > 0:
            self.index=self.index-1
            self.label.setStyleSheet(f"""background-color:{self.color_list[self.index]}""")


if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWinddow()

    sys.exit(app.exec())
