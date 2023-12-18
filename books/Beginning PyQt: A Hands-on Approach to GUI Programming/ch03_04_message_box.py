import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QLineEdit, QMessageBox
from PyQt6.QtGui import QIcon, QFont

class MainWindow(QLineEdit):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("QMessageBox Example")
        self.setWindowIcon(QIcon("images/heart_icon1.png"))

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.catalouge_lbl=QLabel("Author Catalouge", self)
        self.catalouge_lbl.move(100, 10)
        self.catalouge_lbl.setFont(QFont("Arial", 12))

        self.search_lbl=QLabel("Search the index for an author: ", self)
        self.search_lbl.move(20, 40)

        self.author_lbl= QLabel("Name: ", self)
        self.author_lbl.move(20, 75)

        self.author_edit=QLineEdit(self)
        self.author_edit.move(70, 70)
        self.author_edit.resize(250, 25)
        self.author_edit.setPlaceholderText("Enter name as: First Last")

        self.search_btn= QPushButton("Search", self)
        self.search_btn.move(150, 110)
        self.search_btn.clicked.connect(self.search_author)

    
    def search_author(self):
        file= "authors.txt"

        try:
            with open(file, "r") as f:
                authors= [line.rstrip("\n") for line in f]
                if self.author_edit.text() in authors:
                    QMessageBox.information(self, "Author found",
                                             "Author found in catalouge!", QMessageBox.StandardButton.Ok)


                else:
                    answer= QMessageBox.question(self, "Author Not Found",
                        """ <p> Author not found in catalouge. </p>
                            <p> Do you wish to continue? </p>""",
                            QMessageBox.StandardButton.Yes | \
                            QMessageBox.StandardButton.No,
                            QMessageBox.StandardButton.Yes)
                    if answer == QMessageBox.StandardButton.No:
                        print("Closing application.")
                        self.close()
        except FileNotFoundError as error:
            QMessageBox.warning(self, "Error", 
                                
                        f"""<p> File not found. </p>
                            <p> Error: {error} </p>
                            Closing application.""",
                            QMessageBox.StandardButton.Ok)
            self.close()

if __name__ == "__main__":
    app= QApplication(sys.argv)
    window=MainWindow()

    sys.exit(app.exec())