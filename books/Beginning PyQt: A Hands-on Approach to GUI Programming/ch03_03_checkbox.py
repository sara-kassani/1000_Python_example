import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QCheckBox
from PyQt6.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("QCheckbox Example")
        self.setWindowIcon(QIcon("images/heart_icon1.png"))

        self.setUpMainWindow()
        self.show()


    def setUpMainWindow(self):
        self.lbl1= QLabel("Which shifts can you work? \n(Please check all that apply)", self)
        self.lbl1.setWordWrap(True)
        self.lbl1.move(10, 15)

        self.info_lbl=QLabel("", self)
        self.info_lbl.resize(200, 100)
        self.info_lbl.setStyleSheet("border: 1px solid gray")
        self.info_lbl.move(40, 150)


        self.morning_cb= QCheckBox("Morning [8 AM - 2 PM]", self)
        self.morning_cb.move(40, 60)
        self.morning_cb.toggled.connect(self.print_selected)

        self.afternoon_cb= QCheckBox("Afternoon [1 PM - 8 PM]", self)
        self.afternoon_cb.move(40, 80)
        self.afternoon_cb.toggled.connect(self.print_selected)

        self.night_cb=QCheckBox("Night [7 PM - 3 AM]", self)
        self.night_cb.move(40, 100)
        self.night_cb.toggled.connect(self.print_selected)

    def print_selected(self, checked):
        sender= self.sender()  ## use sender() sto determine which widget is sending the signal
        if checked:
            print(f"{sender.text()} Selected.")
            self.info_lbl.setText(f"{sender.text()} Selected.")

        else:
            print(f"{sender.text()} Deselected.")
            self.info_lbl.setText(f"{sender.text()} Deselected.")


if __name__ == "__main__":
    app=QApplication(sys.argv)
    window= MainWindow()

    sys.exit(app.exec())
