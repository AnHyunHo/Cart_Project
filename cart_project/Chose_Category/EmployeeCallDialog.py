import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from DB_Code import *
from Sort_Function import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QDialog
from PyQt5.QtCore import QSize

#직원 호출 클래스 , 이후 스마트폰과 연동하여 직원 호출 계획
class EmployeeCallDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("직원 호출")
        self.setGeometry(100, 100, 300, 150)
        self.message_label = QtWidgets.QLabel("잠시만 기다려 주세요...", self)
        self.message_label.setGeometry(75, 20, 200, 30)
        self.return_button = QtWidgets.QPushButton("돌아가기", self)
        self.return_button.setGeometry(100, 70, 100, 30)
        self.return_button.clicked.connect(self.close)