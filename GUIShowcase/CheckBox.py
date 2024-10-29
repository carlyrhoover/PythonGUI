from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QGridLayout, QMainWindow, QPushButton

import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("Checkbox Art")
        self.setGeometry(100,100,1000,750)
        
        for row in range(3):
            for col in range(3):
                checkbox = QCheckBox()
        
        
        ##buttons can be placed back in later 
        
        """ self.clearBoard = QPushButton("Clear the board!", self)
        self.clearBoard.setGeometry(200, 150, 100, 30)  

        self.invertBoard = QPushButton("Invert the board!", self)
        self.invertBoard.setGeometry(300, 150, 100, 30)  
        
        self.checkBoard = QPushButton("Check the whole board!", self)
        self.checkBoard.setGeometry(400, 150, 150, 30)  """ 
        
def window():   
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
    
window()