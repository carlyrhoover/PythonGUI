from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("Widget Test")
        
        layout = QVBoxLayout()
        widgets = [
            QCheckBox(),
            QComboBox(),
            QDateEdit(),
            QDateTimeEdit(),
            QDial(),
            QDoubleSpinBox(),
            QFontComboBox(),
            QLCDNumber(),
            QLabel("Label"),
            QLineEdit(),
            QProgressBar(),
            QPushButton("Button"),
            QRadioButton(),
            QSlider(),
            QSpinBox(),
            QTimeEdit(),
        ]
        
        for w in widgets: 
            layout.addWidget(w)
            
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()