from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *
from final_win import *
from PyQt5.QtGui import QFont

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.input_age = age
        self.input_tahap1 = test1
        self.input_tahap2 = test2
        self.input_tahap3 = test3

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
        
    def set_appear(self):
        self.setWindowTitle(text_title)
        self.resize(win_width, win_height)
    
    def initUI(self):
        self.lbl_name = QLabel('Enter your full name:')
        self.input_name = QLineEdit('Full Name')
        self.lbl_age = QLabel('Full years')
        self.input_age = QLineEdit('0')
        self.lbl_tahap1 = QLabel('tes detak jantung selama 15 detik')
        self.btn_tahap1 = QPushButton('Start the first test')
        self.input_tahap1 = QLineEdit('0')
        self.lbl_tahap2 = QLabel('tes squat 30 dalam 45 detik, lalu hitung detak jantung')
        self.btn_tahap2 = QPushButton('Start doing squat')
        self.input_tahap2 = QLineEdit('0')
        self.lbl_tahap3 = QLabel('tahap 3')
        self.btn_tahap3 = QPushButton('Start the final test')
        self.input_tahap3 = QLineEdit('0')
        self.button = QPushButton('Send the result')
        self.v_line1 = QVBoxLayout()
        self.v_line1.addWidget(self.lbl_name)
        self.v_line1.addWidget(self.input_name)
        self.v_line1.addWidget(self.lbl_age)
        self.v_line1.addWidget(self.input_age)
        self.v_line1.addWidget(self.lbl_tahap1)
        self.v_line1.addWidget(self.btn_tahap1)
        self.v_line1.addWidget(self.input_tahap1)
        self.v_line1.addWidget(self.lbl_tahap2)
        self.v_line1.addWidget(self.btn_tahap2)
        self.v_line1.addWidget(self.input_tahap2)
        self.v_line1.addWidget(self.lbl_tahap3)
        self.v_line1.addWidget(self.btn_tahap3)
        self.v_line1.addWidget(self.input_tahap3)
        self.v_line1.addWidget(self.button)
        
        self.stopwatch = QLabel('00:00:00')
        self.v_line2 = QVBoxLayout()
        self.v_line2.addWidget(self.stopwatch)
        
        self.h_line = QHBoxLayout()
        self.h_line.addLayout(self.v_line1)
        self.h_line.addLayout(self.v_line2)
        
        self.setLayout(self.h_line)
    
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.stopwatch.setText(time.toString("hh:mm:ss"))
        self.stopwatch.setFont(QFont("Times", 36, QFont.Bold))
        self.stopwatch.setStyleSheet("warna: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
            
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.stopwatch.setText(time.toString("hh:mm:ss")[6:8])
        self.stopwatch.setFont(QFont("Times", 36, QFont.Bold))
        self.stopwatch.setStyleSheet("warna: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
        
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.stopwatch.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.stopwatch.setStyleSheet("warna: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.stopwatch.setStyleSheet("warna: rgb(0,255,0)")
        else:
            self.stopwatch.setStyleSheet("warna: rgb(0,0,0)")
        self.stopwatch.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    
    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
        
    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    
    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    
    def next_click(self):
        self.hide()
        self.exp = Experiment(int(self.input_age.text()), int(self.input_tahap1.text()), int(self.input_tahap2.text()), int(self.input_tahap3.text()))
        self.fw = FinalWin(self.exp)
    
    def connects(self):
        self.button.clicked.connect(self.next_click)
        self.btn_tahap1.clicked.connect(self.timer_test)
        self.btn_tahap2.clicked.connect(self.timer_sits)
        self.btn_tahap3.clicked.connect(self.timer_final)
