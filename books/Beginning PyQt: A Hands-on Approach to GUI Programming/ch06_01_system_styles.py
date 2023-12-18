import sys
from PyQt6.QtWidgets import QApplication, QStyleFactory
print(f"Keys: {QStyleFactory.keys()}")   ## Keys: ['windowsvista', 'Windows', 'Fusion']

app=QApplication(sys.argv)
print(f"Default style: {app.style().name()}")   ## Default style: windowsvista