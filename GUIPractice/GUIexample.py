from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

import sys

def main(): 
    ##basic window 
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    mainWindow.setGeometry(200,200,300,300)
    mainWindow.setWindowTitle("Test Window")

    ##basic text label on window 
    label = QLabel(mainWindow)
    label.setText("Test Label")
    label.move(50,50)
    
    ##makes window visible 
    mainWindow.show()
    sys.exit(app.exec_())
    
    # https://www.techwithtim.net/tutorials/pyqt5-tutorial/basic-gui-application
    
main()