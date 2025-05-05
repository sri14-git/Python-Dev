import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, \
    QMainWindow, QTableWidget, QTableWidgetItem, QAbstractItemView, QDialog, QMessageBox, QComboBox
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        filemenu = self.menuBar().addMenu("&File")
        helpmenu = self.menuBar().addMenu("&Help")
        add_student=QAction("Add Student",self)
        add_student.triggered.connect(self.insert)
        filemenu.addAction(add_student)
        about = QAction("About",self)
        helpmenu.addAction(about)
        about.setMenuRole(QAction.MenuRole.NoRole)
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id","Name","Course","Mobile Number"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)
    def load_data(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        result = cursor.execute("SELECT * FROM Students")
        self.table.setRowCount(0)
        for rowno,row in enumerate(result):
            self.table.insertRow(rowno)
            for colno,value in enumerate(row):
                print(row)
                self.table.setItem(rowno,colno,QTableWidgetItem(str(value)))
        conn.close()
    def insert(self):
        dialog= InsertDialog()
        dialog.exec()

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Student Data")
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        layout = QVBoxLayout()
        self.student_name = QLineEdit(self)
        self.student_name.setPlaceholderText("Student Name")
        layout.addWidget(self.student_name)

        #Combo Box for Courses
        self.course_name = QComboBox()
        course=["Biology","Maths","Astronomy","Physics"]
        self.course_name.addItems(course)
        layout.addWidget(self.course_name)

        #Add Mobile Layout
        self.mobile_number = QLineEdit(self)
        self.mobile_number.setPlaceholderText("Mobile Number")
        layout.addWidget(self.mobile_number)

        # Adding Button for Submit
        button_add = QPushButton(self)
        button_add.setText("Submit")
        button_add.clicked.connect(self.add_student)
        layout.addWidget(button_add)

        self.setLayout(layout)
    def add_student(self):
        name = self.student_name.text()
        mobile_number = self.mobile_number.text()
        course=self.course_name.currentText()
        conn=sqlite3.connect("database.db")
        cursor=conn.cursor()
        cursor.execute("INSERT INTO students(name,course,mobile_number) VALUES(?,?,?)",
                       (name,course,mobile_number))
        conn.commit()
        conn.close()
        window.load_data()
        self.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.load_data()
    sys.exit(app.exec())
