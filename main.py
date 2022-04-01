import sys

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QLineEdit


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.state = "NO"
        self.pre_state = "NO"
        self.exe_op = "EQ"
        self.plan_op = "EQ"
    def debug(self):
        print("pre_state: " + self.pre_state + "  state: " + self.state)
        print("exe_op: " + self.exe_op + "  plan_op: " + self.plan_op)


    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # 버튼 생성
        self.line_edit = QLineEdit("0")
        self.line_edit.setAlignment(Qt.AlignRight)  # 우측으로 정렬

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

        button_list = [self.line_edit, cancelButton, equalButton, button_1, button_2, button_3, button_4, button_5,button_6,button_7,button_8,button_9,button_0,button_Add,button_Sub,button_Div,button_Mul,button_Point,button_Flipsign]
        for i in button_list:
            i.setMaximumHeight(40)
        # 버튼 배치
        grid.addWidget(self.line_edit,0,0,1,0)
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
        button_1.clicked.connect(self.one)
        button_2.clicked.connect(self.two)
        button_3.clicked.connect(self.three)
        button_4.clicked.connect(self.four)
        button_5.clicked.connect(self.five)
        button_6.clicked.connect(self.six)
        button_7.clicked.connect(self.seven)
        button_8.clicked.connect(self.eight)
        button_9.clicked.connect(self.nine)

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

    def convert_int_or_float(testnum):
        if "." not in testnum:
            testnum = int(testnum)
        else:
            testnum = float(testnum)

    # def check_int_or_float(num):
    #     for i in num:
    #         if i =='.':
    #             posi_float = num[i:]
    #             for j in posi_float:
    #                 if j != 0:
    #                     num =float(num)
    #                     print(type(num))
    #                 else:
    #                     num = int(num)
    #                     print(type(num))
    #
    #         else:
    #             num = int(num)
    #             print(type(num))
    #
    #
    # print(check_int_or_float('6.005'))
    # print(check_int_or_float('5.0000'))

    # NO에서 누르면 '.0'이 되어야함 (상태 FN)-> 0-9 누르면 FN , op나 '.'을 눌려도 그대로 유지
    # '.'이 앞에 있으면 다시 못누르게 해야함
    def point(self):
        # pre_state 는 지금 가지고 있는 state값을 넣어주고
        self.pre_state = self.state

        if self.pre_state == "NO":
            #self.lineEdit.setText("0.") 둘다 가능
            lineEdit_num = self.line_edit.text()

            self.line_edit.setText(lineEdit_num + ".")
            self.state = "FN"
        elif self.pre_state == "FN":
            lineEdit_num = self.line_edit.text()

            if "." not in lineEdit_num:
                self.line_edit.setText(lineEdit_num + ".")
                # 굳이 현재 state를 FN으로 바꿔 줘야하나? 이미 FN이기 때문에.. 음..
                # self.state ="FN"
            # else구문이 필요한가요? lineEdit_num 에 이미 . 이 있을 경우 .을 찍으면 안되기 때문에 아무작동 안함
            # else:
            #     return
        elif self.pre_state == "OP":
            self.line_edit.setText("0.")
            self.state = "SN"
        elif self.pre_state == "SN":
            lineEdit_num = self.line_edit.text()

            if "." not in lineEdit_num:
                self.line_edit.setText(lineEdit_num + ".")
                # 굳이 현재 state를 SN으로 바꿔 줘야하나? 이미 SN이기 때문에.. 음..
                # self.state ="SN"


    #"NO"에서 0을 누르면 계속 0이 나와야한다.
    # 숫자 다음 0을 누르면 나와야한다.
    # ".0" 포인트 다음 나오면 나와야한다.
    def zero(self):
        # pre_state 는 지금 가지고 있는 state값을 넣어주고
        self.pre_state = self.state
        lineEdit_num = self.line_edit.text()

        # pre_state가 NO 일때도 필요한가? NO일때는 0을 눌려도 아무작동 일어나지 않음
        if self.pre_state == "FN":
            self.line_edit.setText(lineEdit_num + "0")
            self.state = "FN"
        elif self.pre_state == "OP":
            self.line_edit.setText("0")
            self.state = "SN"
        elif self.pre_state =="SN":
            self.line_edit.setText(lineEdit_num + "0")
            self.state = "SN"

    def one(self):
        self.number('1')
    def two(self):
        self.number('2')
    def three(self):
        self.number('3')
    def four(self):
        self.number('4')
    def five(self):
        self.number('5')
    def six(self):
        self.number('6')
    def seven(self):
        self.number('7')
    def eight(self):
        self.number('8')
    def nine(self):
        self.number('9')

    # "NO"에서 숫자를 누르면 나와야한다.
    def number(self, num):
        # pre_state 는 지금 가지고 있는 state값을 넣어주고
        self.pre_state = self.state
        if self.pre_state == "NO":
            self.line_edit.setText(num)
            self.state = "FN"
        elif self.pre_state == "FN":
            lineEdit_num = self.line_edit.text()
            self.line_edit.setText(lineEdit_num + num)
            self.state = "FN"
        elif self.pre_state == "OP":
            self.line_edit.setText(num)
            self.state = "SN"
        elif self.pre_state == "SN":
            lineEdit_num = self.line_edit.text()
            self.line_edit.setText(lineEdit_num + num)
            self.state = "SN"
        self.debug()


    def flipsign(self):
        pass


    def cancel(self):
        pass

    def result(self):
        self.Operation("NO_OP")

    def Add(self):
        self.Operation("ADD")


    def Sub(self):
        self.Operation("SUB")


    def Mul(self):
        self.Operation("MUL")


    def Div(self):
        self.Operation("DIV")


    def Operation(self, op_type):
        # pre_state 는 지금 가지고 있는 state값을 넣어주고
        self.pre_state = self.state
        # 이 함수에서는 'OP' state를 가져가도록
        self.state = "OP"

        self.exe_op = self.plan_op
        self.plan_op = op_type

        # 지금 가지고 있는 op_type확인
        #if op_type == "ADD":


        # 첫번째 계산에서는 그냥 무슨 연산인지만 저장하고 FN을 val1에 저장
        if self.pre_state == "FN":
            self.val1 = self.line_edit.text()
            # 여기서 op_state가 아니라 누른 버튼이 +인지 -인지를 구분해내서 그거를 저장해둬야함
            # 연산 버튼을 눌렸을 때 그것이 + 인지 - 인지 알아내는걸 어떻게 해야하지..
        # 두번째 계산이면 앞의 op_state에 따라서 계산을 해주고 나갈때는 또 지금 op_state를 넣어두면 됨
        elif self.pre_state == "SN":
            self.val2 = self.line_edit.text()
            if self.exe_op == "ADD":
                self.val1 = self.val1 + self.val2
            elif self.exe_op == "SUB":
                self.val1 = self.val1 - self.val2
            elif self.exe_op == "MUL":
                self.val1 = self.val1 * self.val2
            elif self.exe_op == "DIV":
                self.val1 = self.val1 / self.val2

            # '='을 누를때는 어떻게 작동?
            #elif self.exe_op == "NO_OP":

            #op_state 1차를 계산해서 결과값을 돌려주고, 2차 op를 눌린거니까 그 2차 op를 저장해둬
            self.val1 = self.convert_int_or_float(self.val1)
            self.line_edit.setText(self.val1)
        self.debug()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())