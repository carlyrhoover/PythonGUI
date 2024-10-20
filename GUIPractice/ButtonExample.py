from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import choice

import sys

##button titles outside class 
buttonTitles = [  
        "Ouch!",
        "Hey! Easy!",
        "How would you like it?!",
        "Don't try it!",
        "Yeowch!",
        "That hurts!!"
        ]

class MyWindow(QMainWindow): 
    
    
    def __init__(self):  # Fixed the typo here
        super(MyWindow, self).__init__()
        self.initUI()
        
    ##the button will remain clicked until otherwise 
    def button_clicked(self):
        print("Button has been clicked.")
        self.label.setText("That was rude, man.")
        
        updatedButtonText = choice(buttonTitles)
        self.button.setText(updatedButtonText)
        self.button.adjustSize()
        self.update()
        
    ##update the text based on the button being pressed
    def update(self):
        self.label.adjustSize()
        
    def initUI(self):
        # Basic window settings
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Window Test")

        # Basic text label on the window
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hey, man, what's up?")
        self.label.move(50, 50)
        self.label.adjustSize()
        
        # Basic button example
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Hey, dude!")
        self.button.move(50, 100)  # Added move to position the button
        self.button.clicked.connect(self.button_clicked)

# Main function to run the window
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
        

    