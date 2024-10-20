from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

import sys

def main(): 
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    mainWindow.setGeometry(200,200,300,300)
    mainWindow.setWindowTitle("Test Window")

    label = QLabel(mainWindow)
    label.setText("Test Label")
    label.move(50,50)
    
    mainWindow.show()
    sys.exit(app.exec_())
    
main()