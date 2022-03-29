import sys

from PySide6.QtCore import *
from PySide6.QtWidgets import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.state = "NO"
        self.pre_state = "NO"
        self.op_state = "EQ"
        self.pre_op_state = "EQ"

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
        button_0.clicked.connect(self.zero)
        button_1.clicked.connect(self.number)
        button_Point.clicked.connect(self.point)
        button_Flipsign.clicked.connect(self.flipsign)
        button_Add.clicked.connect(self.Add)
        button_Sub.clicked.connect(self.Sub)
        button_Mul.clicked.connect(self.Mul)
        button_Div.clicked.connect(self.Div)

        # 창 만들기
        self.setWindowTitle('Calculator')
        self.setGeometry(1000, 200, 150, 300)
        self.show()

    #"NO"에서 0을 누르면 계속 0이 나와야한다.
    # 숫자 다음 0을 누르면 나와야한다.
    # ".0" 포인트 다음 나오면 나와야한다.
    def zero(self):
        pass
    # "NO"에서 숫자를 누르면 나와야한다.
    def number(self):
        pass

    def point(self):
        pass

    def flipsign(self):
        pass


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

    def Operation(self):
        # pre_state 는 지금 가지고 있는 state값을 넣어주고
        self.pre_state = self.state
        # 이 함수에서는 'OP' state를 가져가도록
        self.state = "OP"

        # 지금 가지고 있는 OP_state확인

        # 첫번째 계산에서는 그냥 무슨 연산인지만 저장하고 FN을 val1에 저장
        if self.pre_state == "FN":
            self.val1 = self.lineEdit.text()
            # 여기서 op_state가 아니라 누른 버튼이 +인지 -인지를 구분해내서 그거를 저장해둬야함
            # 연산 버튼을 눌렸을 때 그것이 + 인지 - 인지 알아내는걸 어떻게 해야하지..?
            if self.op_state == "ADD":
                self.op_state == "ADD"
            elif self.op_state == "SUB":
                self.op_state == "SUB"
            elif self.op_state =="MUL":
                self.op_state == "MUL"
            elif self.op_state == "DIV":
                self.op_state == "DIV"
            elif self.op_state == "EQ":
                self.op_state == "EQ"
        # 두번째 계산이면 앞의 op_state에 따라서 계산을 해주고 나갈때는 또 지금 op_state를 넣어두면 됨
        elif self.pre_state == "SN":
            self.val2 = self.lineEdit.text()
            if self.op_state == "ADD":
                self.val2 = self.val1 + self.val2
            elif self.op_state == "SUB":
                self.val2 = self.val1 - self.val2
            elif self.op_state =="MUL":
                self.val2 = self.val1 * self.val2
            elif self.op_state == "DIV":
                self.val2 = self.val1 / self.val2
            #op_state 1차를 계산해서 결과값을 돌려주고, 2차 op를 눌린거니까 그 2차 op를 저장해둬


            self.lineEdit.setText(self.val2)


    def make_num_button(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())