import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox, QButtonGroup, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 500, 200)
        self.setWindowTitle("QVBoxLayout Example")
        self.setWindowIcon(QIcon("images/heart_icon1.png"))
        

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.lbl_header= QLabel("PyQt6 Course", self)
        self.lbl_header.setFont(QFont("Arial", 16))
        self.lbl_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lbl_question=QLabel("How would you rate this course?", self)
        self.lbl_question.setAlignment(Qt.AlignmentFlag.AlignTop)

        ratings= ["Satisfied", "Average", "Not Satisfied"]
        ratings_group= QButtonGroup(self)
        ratings_group.buttonClicked.connect(self.checkbox_clicked)

        self.btn_confirm= QPushButton("Confirm", self)
        self.btn_confirm.setEnabled(False)
        self.btn_confirm.clicked.connect(self.close)

        main_vbox= QVBoxLayout()
        main_vbox.addWidget(self.lbl_header)
        main_vbox.addWidget(self.lbl_question)

        for cb in range(len(ratings)): # cb is 0, 1, 2
            cb_rating= QCheckBox(ratings[cb])
            ratings_group.addButton(cb_rating)
            main_vbox.addWidget(cb_rating)

        main_vbox.addWidget(self.btn_confirm)

        self.setLayout(main_vbox)

    def checkbox_clicked(self, button):
        print(button.text())
        self.btn_confirm.setEnabled(True)





if __name__ == "__main__":
    app=QApplication(sys.argv)
    window= MainWindow()

    sys.exit(app.exec())        

        