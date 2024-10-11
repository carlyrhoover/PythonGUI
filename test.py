import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.buttonClicked)
        button.clicked.connect(self.buttonToggled)


        # Set the central widget of the Window.
        self.setCentralWidget(button)
        
        ##also consider .setMinimumSize() as well as .setMaximumSize()
        self.setFixedSize(QSize(400,300))

    def buttonClicked(self):
        print("Clicked")
            
    def buttonToggled(self, checked):
        print("Checked?", checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()