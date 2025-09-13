from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from instr import *
from second_win import TestWin

class MainWin(QWidget):
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
        self.hello_text = QLabel('Welcome to tes ruffier app')
        self.instruction = QLabel('The Application allow use...')
        self.button = QPushButton('Start')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
    
    def next_click(self):
        self.hide()
        self.tw = TestWin()
    
    def connects(self):
        self.button.clicked.connect(self.next_click)
    
app = QApplication([])
win = MainWin()
app.exec_()
