import sys
from datetime import datetime

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        # Need Grid to Add Widgets
        grid = QGridLayout()
        self.setWindowTitle("Age Calculator")

        # Create Widgets
        name_label = QLabel("Name: ")
        self.name_lineedit = QLineEdit()
        dob_label = QLabel("DOB(YYYY-MM-DD): ")
        self.dob_lineedit = QLineEdit()

        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate)
        self.outputlabel = QLabel("")
        # Adding Widgets to the Grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_lineedit, 0, 1)
        grid.addWidget(dob_label, 1, 0)
        grid.addWidget(self.dob_lineedit, 1, 1)
        grid.addWidget(calculate_button, 2, 0,1,2)
        grid.addWidget(self.outputlabel, 3, 0,1,2)
        self.setLayout(grid)

    def calculate(self):
        current_year = datetime.today().year
        print(current_year)
        yearofbirth = self.dob_lineedit.text()
        yearofbirth= datetime.strptime(yearofbirth, "%Y-%m-%d").date().year
        print(yearofbirth)
        age = current_year - yearofbirth
        # self.outputlabel.setText(f"{self.name_lineedit.text()} Age is {age}")
        self.outputlabel.setText(f"{self.name_lineedit.text()} is {age} years old")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AgeCalculator()
    window.show()
    sys.exit(app.exec())