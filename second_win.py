from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *
from final_win import FinalWin

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
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
        
        self.stopwatch = QLabel('00:00:09')
        self.v_line2 = QVBoxLayout()
        self.v_line2.addWidget(self.stopwatch)
        
        self.h_line = QHBoxLayout()
        self.h_line.addLayout(self.v_line1)
        self.h_line.addLayout(self.v_line2)
        
        self.setLayout(self.h_line)
        
        
    
    def next_click(self):
        self.hide()
        self.fw = FinalWin()
    
    def connects(self):
        self.button.clicked.connect(self.next_click)

