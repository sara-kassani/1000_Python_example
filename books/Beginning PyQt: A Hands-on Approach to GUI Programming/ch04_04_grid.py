import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QTextEdit, QGridLayout)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QIcon, QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(500, 300)
        self.setWindowTitle("QGridLayout Example")
        self.setWindowIcon(QIcon("images/heart_icon1.png"))

        self.setUpMainWindow()
        self.loadWidgetValuesFromFile()
        self.show()

    def setUpMainWindow(self):
        self.lbl_name=QLabel("Simple Daily Planner",self)
        self.lbl_name.setFont(QFont("Arial", 12))
        self.lbl_name.setAlignment(Qt.AlignmentFlag.AlignLeft)


        ## left widgets
        self.lbl_today=QLabel("Today's Focus", self)
        self.lbl_today.setFont(QFont("Arial", 10))
        self.edit_today=QTextEdit()

        self.lbl_notes=QLabel("Notes", self)
        self.setFont(QFont("Arial", 10))
        self.edit_notes= QTextEdit()

        ##organize the left side widgets into column 0 of hte QGridLayout
        self.main_grid= QGridLayout()
        self.main_grid.addWidget(self.lbl_name, 0, 0)
        self.main_grid.addWidget(self.lbl_today, 1, 0)
        self.main_grid.addWidget(self.edit_today, 2, 0, 3, 1)
        self.main_grid.addWidget(self.lbl_notes, 5, 0)
        self.main_grid.addWidget(self.edit_notes, 6, 0, 3, 1)

        ## write widgets
        today=QDate.currentDate().toString(Qt.DateFormat.ISODate)
        self.lbl_date=QLabel(today, self)
        self.lbl_date.setFont(QFont("Arial", 10))
        self.lbl_date.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.lbl_todo=QLabel("To Do", self)
        self.lbl_todo.setFont(QFont("Arial", 10))

        ## organize the right side widgets into columns 1 and 2 of the QGridLayout
        self.main_grid.addWidget(self.lbl_date, 0, 2)
        self.main_grid.addWidget(self.lbl_todo, 1, 1, 1, 2)

        ## create 7 rows, from indexes 2-8
        for row in range(2, 9):
            item_cb= QCheckBox()
            item_edit=QLineEdit()
            self.main_grid.addWidget(item_cb, row, 1)
            self.main_grid.addWidget(item_edit, row, 2)

        self.setLayout(self.main_grid)

    def loadWidgetValuesFromFile(self):
        pass



if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()

    sys.exit(app.exec())