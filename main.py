import sys

from PySide6.QtCore import *
from PySide6.QtWidgets import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.state = "NO"
        self.pre_state = "NO"

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # 버튼 생성
        lineEdit = QLineEdit("0")
        lineEdit.setAlignment(Qt.AlignRight)  # 우측으로 정렬

        cancelButton = QPushButton('C')
        equalButton = QPushButton('=')

        button_1 = QPushButton('1')
        button_2 = QPushButton('2')
        button_3 = QPushButton('3')
        button_4 = QPushButton('4')
        button_5 = QPushButton('5')
        button_6 = QPushButton('6')
        button_7 = QPushButton('7')
        button_8 = QPushButton('8')
        button_9 = QPushButton('9')
        button_0 = QPushButton('0')

        button_Add = QPushButton('+')
        button_Sub = QPushButton('-')
        button_Mul = QPushButton('X')
        button_Div = QPushButton('/')

        button_Point = QPushButton('.')
        button_Flipsign = QPushButton('+/-')

        button_list = [lineEdit, cancelButton, equalButton,button_1, button_2, button_3,button_4,button_5,button_6,button_7,button_8,button_9,button_0,button_Add,button_Sub,button_Div,button_Mul,button_Point,button_Flipsign]
        for i in button_list:
            i.setMaximumHeight(40)
        # 버튼 배치
        grid.addWidget(lineEdit,0,0,1,0)
        grid.addWidget(cancelButton,1,0,1,2)
        grid.addWidget(equalButton,1,2,1,2)

        grid.addWidget(button_1,4,0,1,1)
        grid.addWidget(button_2,4,1,1,1)
        grid.addWidget(button_3,4,2,1,1)
        grid.addWidget(button_4,3,0,1,1)
        grid.addWidget(button_5,3,1,1,1)
        grid.addWidget(button_6,3,2,1,1)
        grid.addWidget(button_7,2,0,1,1)
        grid.addWidget(button_8,2,1,1,1)
        grid.addWidget(button_9,2,2,1,1)
        grid.addWidget(button_0,5,1,1,1)

        grid.addWidget(button_Add,4,3,1,1)
        grid.addWidget(button_Sub,5,3,1,1)
        grid.addWidget(button_Mul,3,3,1,1)
        grid.addWidget(button_Div,2,3,1,1)

        grid.addWidget(button_Point,5,2,1,1)
        grid.addWidget(button_Flipsign,5,0,1,1)

        # Button event handle
        cancelButton.clicked.connect(self.cancel)
        equalButton.clicked.connect(self.result)
        for i in range(10):
            button = 'button_' + i
            button.clicked.connect(self.buttoni)
        button_Add.clicked.connect(self.Add)
        button_Sub.clicked.connect(self.Sub)
        button_Mul.clicked.connect(self.Mul)
        button_Div.clicked.connect(self.Div)

        # 창 만들기
        self.setWindowTitle('Calculator')
        self.setGeometry(1000, 200, 150, 300)
        self.show()

    def cancel(self):
        pass

    def result(self):
        pass

    def Add(self):
        pass

    def sub(self):
        pass

    def Mul(self):
        pass

    def Div(self):
        pass

    def make_num_button(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())