import random

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QLineEdit, QSlider, QLabel, QCheckBox


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.line_edit = QLineEdit()

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.label = QLabel("123")

        self.checkbox_capital = QCheckBox("Großbuchstaben")
        self.checkbox_small = QCheckBox("Kleinbuchstaben")
        self.checkbox_numbers = QCheckBox("Ziffern")
        self.checkbox_special = QCheckBox("Sonderzeichen")

        gridlayout = QGridLayout()
        gridlayout.addWidget(self.line_edit, 1, 1, 1, 4)
        gridlayout.addWidget(self.label, 2, 1, Qt.AlignmentFlag.AlignRight)
        gridlayout.addWidget(self.slider, 2, 2, 1, 3)
        gridlayout.addWidget(self.checkbox_capital, 3, 1)
        gridlayout.addWidget(self.checkbox_small, 3, 2)
        gridlayout.addWidget(self.checkbox_numbers, 3, 3)
        gridlayout.addWidget(self.checkbox_special, 3, 4)

        self.setLayout(gridlayout)
