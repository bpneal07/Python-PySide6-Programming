#Version1: Just responding to the button click : syntax

"""
from PySide6.QtWidgets import QApplication, QPushButton

#The slot : responds when something happens
def button_clicked():
    print("You clicked the button, didn't you!")

app = QApplication()
button = QPushButton("Press Me")

#Clicked is a signal of QPushButton. It's emitted when you click
# on the button
#You can wire a lot to the signal using the syntax below :
button.clicked.connect(button_clicked)

button.show()
app.exec()
"""

#Version2: Signals sending values, capture values in slots
"""
from PySide6.QtWidgets import QApplication, QPushButton

def button_clicked(data):
    print("You clicked the button, didn't you! checked : ", data)

app = QApplication()
button = QPushButton("Press Me")
button.setCheckable(True) # Makes the button checkable. It's unchecked by the default.
                              # Further clicks toggle between checked and unchecked states.

#clicked is a signal of QPushBUtton. It's emitted when you click on the button
#You can wire a slot to the signal using the syntax below :
button.clicked.connect(button_clicked)

button.show()
app.exec()
"""


#Version3: Capture value from a slider
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

#The slot : responds when something happens
def respond_to_slider(data):
    print("Slider moved to : ", data)
app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

#You just do the connection. The Qt system takes care of
# passing the data from the signal to the slot.
slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()
