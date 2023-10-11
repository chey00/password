import random

from PyQt6.QtCore import Qt, pyqtSlot
from PyQt6.QtWidgets import QWidget, QGridLayout, QLineEdit, QSlider, QLabel, QCheckBox


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.set_capital = ["A", "B", "C", "D"]
        self.set_small = ["a", "b", "c", "d"]
        self.set_number = ["1", "2", "3", "4"]
        self.set_special = ["!", "§", "$", "%"]

        self.checked_capital = True
        self.checked_small = True
        self.checked_number = True
        self.checked_special = True

        self.line_edit = QLineEdit()

        self.label = QLabel()

        self.length = 10

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.valueChanged.connect(self.set_label)
        self.slider.setRange(1, 25)
        self.slider.setValue(self.length)

        self.checkbox_capital = QCheckBox("Großbuchstaben")
        self.checkbox_small = QCheckBox("Kleinbuchstaben")
        self.checkbox_numbers = QCheckBox("Ziffern")
        self.checkbox_special = QCheckBox("Sonderzeichen")

        self.checkbox_capital.setChecked(self.checked_capital)
        self.checkbox_small.setChecked(self.checked_small)
        self.checkbox_numbers.setChecked(self.checked_number)
        self.checkbox_special.setChecked(self.checked_special)

        self.checkbox_capital.clicked.connect(self.set_checked_capital)
        self.checkbox_small.clicked.connect(self.set_checked_small)
        self.checkbox_numbers.clicked.connect(self.set_checked_number)
        self.checkbox_special.clicked.connect(self.set_checked_special)

        gridlayout = QGridLayout()
        gridlayout.addWidget(self.line_edit, 1, 1, 1, 4)
        gridlayout.addWidget(self.label, 2, 1, Qt.AlignmentFlag.AlignRight)
        gridlayout.addWidget(self.slider, 2, 2, 1, 3)
        gridlayout.addWidget(self.checkbox_capital, 3, 1)
        gridlayout.addWidget(self.checkbox_small, 3, 2)
        gridlayout.addWidget(self.checkbox_numbers, 3, 3)
        gridlayout.addWidget(self.checkbox_special, 3, 4)

        self.setLayout(gridlayout)

    def set_checked_capital(self):
        if self.checked_capital:
            self.checkbox_capital = False
        else:
            self.checkbox_capital = True

        self.generate_password()

    def set_checked_small(self):
        if self.checked_small:
            self.checked_small = False
        else:
            self.checked_small = True

        self.generate_password()

    def set_checked_number(self):
        if self.checked_number:
            self.checked_number = False
        else:
            self.checked_number = True

        self.generate_password()

    def set_checked_special(self):
        if self.checked_special:
            self.checked_special = False
        else:
            self.checked_special = True

        self.generate_password()

    def set_label(self, value):
        self.length = value

        str_value = str(value)
        self.label.setText(str_value)

        self.generate_password()

    def generate_password(self):
        chars = list()

        if self.checked_capital:
            chars += self.set_capital

        if self.checked_small:
            chars += self.set_small

        if self.checked_number:
            chars += self.set_number

        if self.checked_special:
            chars += self.set_special

        password = ""
        for _ in range(self.length):
            random_value = random.randint(1, len(chars))

            password += chars[random_value - 1]

        self.line_edit.setText(password)
