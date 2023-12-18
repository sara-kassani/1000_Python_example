import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QComboBox, 
                             QSpinBox, QDoubleSpinBox, QStackedLayout, QFormLayout, QVBoxLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setFixedSize(300, 350)
        self.setWindowTitle("QStackedLayout Example")
        self.setWindowIcon(QIcon("images/cute_dog5.jpg"))

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        page_combo=QComboBox()
        page_combo.addItems(["Images", "Description", "Additional Info"])
        page_combo.activated.connect(self.switch_page)


        ## create the Image Page (Page 1)
        profile_img=QLabel()
        pixmap=QPixmap("images/cute1.png")
        profile_img.setPixmap(pixmap)
        profile_img.setScaledContents(True)


        ## create the Profile Page (Page 2)
        profile_form=QFormLayout()
        profile_form.setFieldGrowthPolicy(
            QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        profile_form.setFormAlignment(
            Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

        profile_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)

        profile_form.addRow("Breed:", QLabel("Norwegian Forest Cat"))
        profile_form.addRow("Origin:", QLabel("Norway"))
        profile_form.addRow(QLabel("Description:"))
        default_text="""Have a long, sturdy body, long legs and a bushy tail. 
        They are friendly, intelligent, and generally good with people.""" 
        profile_form.addRow(QTextEdit(default_text))   

        page2_container=QWidget()
        page2_container.setLayout(profile_form)

        ## create the About Page (Page 3)
        about_form=QFormLayout()
        about_form.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        about_form.setFormAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        about_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)

        about_form.addRow(QLabel("Enter your cat's info."))
        about_form.addRow("Name:", QLineEdit())
        about_form.addRow("Color:", QLineEdit())

        age_sb=QSpinBox()
        age_sb.setRange(0, 30)
        about_form.addRow("Age:", age_sb)

        weight_dsb=QDoubleSpinBox()
        weight_dsb.setRange(0.0, 30.0)
        about_form.addRow("Weight (kg):", weight_dsb)

        page3_container=QWidget()
        page3_container.setLayout(about_form)


        ## create the stacked layout and add pages
        self.stacked_layout=QStackedLayout()
        self.stacked_layout.addWidget(profile_img)
        self.stacked_layout.addWidget(page2_container)
        self.stacked_layout.addWidget(page3_container)


        ## add widgets and the stacked layout to the main layout
        main_v_box=QVBoxLayout()
        main_v_box.addWidget(page_combo)
        main_v_box.addLayout(self.stacked_layout)

        self.setLayout(main_v_box)

    def switch_page(self, index):
        self.stacked_layout.setCurrentIndex(index)
        

if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()

    sys.exit(app.exec())