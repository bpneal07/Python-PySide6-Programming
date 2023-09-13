
#Importing the components we need
from PySide6.QtWidgets import QApplication, QWidget

#The sys module is responsible for processing command line arguments
import sys

#It is the wrapper that runs all the functions of the application
app = QApplication(sys.argv)

window = QWidget()
window.show()

#It starts the while event loop that runs the application
app.exec()