import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QSpinBox, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        # self.setGeometry(100, 100, 500, 400)
        self.setMinimumSize(400, 160)
        self.setWindowTitle("Nested Layout Example")
        self.setWindowIcon(QIcon("images/heart_icon1.png"))

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.lbl_info= QLabel("Select 2 items for lunch and their prices.", self)
        self.lbl_info.setFont(QFont("Arial", 12))
        self.lbl_info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        food_list=["egg", "turkey sandwich", "ham sandwich", "cheese", "hummus", "yougurt", "apple",
                   "banana", "orange", "waffle", "carrots", "bread", "pasta", "crackers", "pretzels", 
                   "coffee", "soda", "water"]
        
        self.food_combo1= QComboBox(self)
        self.food_combo1.addItems(food_list)

        self.food_combo2= QComboBox(self)
        self.food_combo2.addItems(food_list)


        self.price_sb1= QSpinBox(self)
        self.price_sb1.setRange(0, 100)
        self.price_sb1.setPrefix("$")
        self.price_sb1.valueChanged.connect(self.calculate_total)

        self.price_sb2= QSpinBox(self)
        self.price_sb2.setRange(0, 100)
        self.price_sb2.setPrefix("$")
        self.price_sb2.valueChanged.connect(self.calculate_total)

        self.lbl_total=QLabel("Total spent: $ ", self)
        self.lbl_total.setFont(QFont("Arial", 14))
        self.lbl_total.setAlignment(Qt.AlignmentFlag.AlignRight)


        h_box1=QHBoxLayout()
        h_box1.addWidget(self.food_combo1)
        h_box1.addWidget(self.price_sb1)

        h_box2=QHBoxLayout()
        h_box2.addWidget(self.food_combo2)
        h_box2.addWidget(self.price_sb2)

        main_vbox=QVBoxLayout()
        main_vbox.addWidget(self.lbl_info)
        main_vbox.addLayout(h_box1)
        main_vbox.addLayout(h_box2)
        main_vbox.addWidget(self.lbl_total)

        self.setLayout(main_vbox)

    def calculate_total(self):
        total= self.price_sb1.value() + self.price_sb2.value()
        self.lbl_total.setText(f"Total spent ${total}")


if __name__ == "__main__":
    app= QApplication(sys.argv)
    window= MainWindow()
    sys.exit(app.exec())
