# import sys
# import random
# from PySide2 import QtCore, QtWidgets, QtGui
# class MyWidget(QtWidgets.QWidget):
    # def __init__(self):
        # super().__init__()

        # self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        # self.button = QtWidgets.QPushButton("Click me!")
        # self.text = QtWidgets.QLabel("Hello World")
        # self.text.setAlignment(QtCore.Qt.AlignCenter)

        # self.layout = QtWidgets.QVBoxLayout()
        # self.layout.addWidget(self.text)
        # self.layout.addWidget(self.button)
        # self.setLayout(self.layout)

        # self.button.clicked.connect(self.magic)


    # def magic(self):
        # self.text.setText(random.choice(self.hello))
# if __name__ == "__main__":
    # app = QtWidgets.QApplication([])

    # widget = MyWidget()
    # widget.resize(800, 600)
    # widget.show()

    # sys.exit(app.exec_())
# import sys
# from PySide2.QtWidgets import QApplication, QLabel

# app = QApplication(sys.argv)
# label = QLabel("Hello World!")
# label.show()
# app.exec_()
# app = QApplication([])
# label = QLabel("<font color=red size=40>Hello World!</font>")
import sys
from PySide2 import QtCore, QtGui, QtWidgets


class LCDRange(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        lcd = QtWidgets.QLCDNumber(2)
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        slider.setRange(0, 99)
        slider.setValue(0)
        self.connect(slider, QtCore.SIGNAL("valueChanged(int)"),
                     lcd, QtCore.SLOT("display(int)"))

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(slider)
        self.setLayout(layout)


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        quit = QtWidgets.QPushButton("Quit")
        quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))
        self.connect(quit, QtCore.SIGNAL("clicked()"),
                     QtWidgets.qApp, QtCore.SLOT("quit()"))

        grid = QtWidgets.QGridLayout()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(quit)
        layout.addLayout(grid)
        self.setLayout(layout)
        for row in range(3):
            for column in range(3):
                grid.addWidget(LCDRange(), row, column)


app = QtWidgets.QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())
# import sys
# from PySide2.QtCore import Qt, Slot
# from PySide2.QtGui import QPainter
 
# app = QApplication(sys.argv)
# widget = QWidget()
# widget.resize(250,150)
# widget.setWindowTitle("Hello World")
# label = QLabel("<font color=red size=30>Hello world </font>",widget)
# label.move(50,50)
# widget.show()
# sys.exit(app.exec_())