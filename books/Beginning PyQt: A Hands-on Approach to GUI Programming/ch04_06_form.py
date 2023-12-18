import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QDateEdit, QLineEdit,
                             QTextEdit, QComboBox, QFormLayout, QHBoxLayout)
from PyQt6.QtCore import Qt, QRegularExpression, QDate
from PyQt6.QtGui import QFont, QIcon, QRegularExpressionValidator

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(500, 400)
        self.setWindowTitle("QFormLayout Example")
        self.setWindowIcon(QIcon("images/heart_icon1.png"))

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.lbl_header= QLabel("Appointment Form", self)
        self.lbl_header.setFont(QFont("Arial", 12))
        self.lbl_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fname_edit=QLineEdit()
        self.fname_edit.setPlaceholderText("First Name")
        self.fname_edit.textEdited.connect(self.clear_text)

        self.lname_edit=QLineEdit()
        self.lname_edit.setPlaceholderText("Last Name")
        self.lname_edit.textEdited.connect(self.clear_text)

        ## create horizontal layout for names
        name_h_box=QHBoxLayout()
        name_h_box.addWidget(self.fname_edit)
        name_h_box.addWidget(self.lname_edit)

        gender_combo=QComboBox()
        gender_combo.addItems(["Male", "Female"])


        self.phone_edit=QLineEdit()
        self.phone_edit.setInputMask("(999) 999-9999;-")
        self.phone_edit.textEdited.connect(self.clear_text)

        self.birthdate_edit=QDateEdit()
        self.birthdate_edit.setDisplayFormat("MM/dd/yyyy")
        self.birthdate_edit.setMaximumDate(QDate.currentDate())
        self.birthdate_edit.setCalendarPopup(True)
        self.birthdate_edit.setDate(QDate.currentDate())

        self.email_edit=QLineEdit()
        self.email_edit.setPlaceholderText("<username>@<domain>.com")
        reg_opt=QRegularExpression()
        regex=QRegularExpression(
            "\\b [A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[com]{3}\\b",
            reg_opt.PatternOption.CaseInsensitiveOption)
        self.email_edit.setValidator(QRegularExpressionValidator(regex))
        self.email_edit.textEdited.connect(self.clear_text)

        extra_info_tedit=QTextEdit()
        
        self.lbl_feedback=QLabel()

        submit_btn=QPushButton("Submit")
        submit_btn.setMaximumWidth(140)
        submit_btn.clicked.connect(self.check_form_information)

        ## create horizontal layout for last row of widgets
        submit_h_box=QHBoxLayout()
        submit_h_box.addWidget(self.lbl_feedback)
        submit_h_box.addWidget(submit_btn)

        main_form=QFormLayout()
        main_form.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        main_form.setFormAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        main_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)

        main_form.addRow(self.lbl_header)
        main_form.addRow("Name", name_h_box)
        main_form.addRow("Gender", gender_combo)
        main_form.addRow("Date of Birth", self.birthdate_edit)
        main_form.addRow("Phone", self.phone_edit)
        main_form.addRow("Emai", self.email_edit)
        main_form.addRow(QLabel("Comments"))
        main_form.addRow(extra_info_tedit)
        main_form.addRow(submit_h_box)

        self.setLayout(main_form)

    def clear_text(self, text):
        self.lbl_feedback.clear()

    def check_form_information(self):
        if self.fname_edit.text() =="" or self.lname_edit.text()=="":
            self.lbl_feedback.setText("Error: Missing names")

        elif self.phone_edit.hasAcceptableInput() == False:
            self.lbl_feedback.setText("Error: Phone number entered incorrectly.")

        elif self.email_edit.hasAcceptableInput() == False:
            self.lbl_feedback.setText("Error: Email entered incorrectly.")

if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()

    sys.exit(app.exec())
