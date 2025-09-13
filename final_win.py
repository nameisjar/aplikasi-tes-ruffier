from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from instr import *

class FinalWin(QWidget):
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
        self.index = QLabel('Ruffier index: 0')
        self.result = QLabel('cardiac performance: there is no data for this age')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.result, alignment=Qt.AlignCenter)
        
        self.setLayout(self.layout)
    
    def next_click(self):
        pass
    
    def connects(self):
        pass

