from PyQt5.QtWidgets import QApplication, QWidget
import sys

##only need one QApplication per file 
app = QApplication(sys.argv)

window = QWidget()
window.show() ##windows are hidden by default

app.exec()