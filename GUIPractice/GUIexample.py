from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class MyWindow(QMainWindow): 
    def __init__(self):  # Fixed the typo here
        super(MyWindow, self).__init__()
        self.initUI()
        
    ##the button will remain clicked until otherwise 
    def button_clicked(self):
        print("Button has been clicked.")
        self.label.setText("The button has been pressed.")
        self.update()
        
    def update(self):
        self.label.adjustSize()
        
    def initUI(self):
        # Basic window settings
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Window Test")

        # Basic text label on the window
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Test Label")
        self.label.move(50, 50)
        
        # Basic button example
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Click Button!")
        self.button.move(50, 100)  # Added move to position the button
        self.button.clicked.connect(self.button_clicked)

# Main function to run the window
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
        
# https://www.techwithtim.net/tutorials/pyqt5-tutorial/basic-gui-application
    