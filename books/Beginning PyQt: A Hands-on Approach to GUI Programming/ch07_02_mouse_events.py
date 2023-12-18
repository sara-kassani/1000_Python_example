import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(400, 300)
        self.setWindowTitle("Evant Handling - Mouse")
        
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.img_lbl=QLabel()
        self.img_lbl.setPixmap(QPixmap("images/cute_dog3.jpg"))

        self.info_lbl=QLabel("")
        self.info_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.pos_lbl=QLabel("")
        self.pos_lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        

        main_v_box=QVBoxLayout()
        main_v_box.addWidget(self.img_lbl)
        main_v_box.addStretch()
        main_v_box.addWidget(self.info_lbl)
        main_v_box.addWidget(self.pos_lbl)

        self.setLayout(main_v_box)

    def enterEvent(self, event):
        self.img_lbl.setPixmap(QPixmap("images/cute_Dog4.jpg"))
    
    def leaveEvent(self, event):
        self.img_lbl.setPixmap(QPixmap("images/cute_dog3.jpg"))

    def mouseMoveEvent(self, event):
        """Print teh mouse position while clicked and moving"""
        if self.underMouse():
            self.pos_lbl.setText(
                f"""<p>X:{event.position().x()},
                Y:{event.position().y()} </p>""")
            
    def mouesPressEvent(self, event):
        """Determine which button was clicked"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.info_lbl.setText("<b> left click </b>")

        if event.button() ==Qt.MouseButton.RightButton:
            self.info_lbl.setText("<b> right click </b>")

    def mouseReleaseEvent(self, event):
        """Determine which button was released."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.info_lbl.setText("<b> Left button released </b>")

        if event.button() == Qt.MouseButton.RightButton:
            self.info_lbl.setText("<b> Right button released </b>")

    def mouseDoubleClickEvent(self, event):
        self.img_lbl.setPixmap(QPixmap("images/cute_dog6.jpg"))

if __name__ == "__main__":
    app=QApplication(sys.argv)
    window=MainWindow()

    sys.exit(app.exec())