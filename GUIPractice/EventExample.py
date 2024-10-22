from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMainWindow

import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(400,400,500,500)
        self.setWindowTitle("Event Test")
        
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)
        
    ##when mouse is moved and being pressed 
    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")
        
    ##when mouse is pressed 
    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")
        
    ##mouse is released
    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")
    
    ##mouse is doubled clicked
    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")
        
##main function 
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
    
window()
        
    
