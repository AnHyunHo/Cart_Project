import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from PyQt5.QtWidgets import *
from PyQt5 import uic
from DB_Code import *
from Sort_Function import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QDialog
from PyQt5.QtCore import QSize

#제품 확인 클래스
class Checking_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("상품 확인")
        self.setGeometry(100, 100, 400, 400)
        self.grid_layout = QGridLayout(self)
        categories = ["가전", "음식", "의류", "생필품"]
        
        self.table = None  # Initialize table as an instance variable
        #카테고리 클릭시 이벤트 발생
        row, col = 0, 0
        for category in categories:
            button = QPushButton(category, self)
            button.clicked.connect(lambda _, cat=category: self.category_clicked(cat))
            button.setFixedSize(QSize(150, 150))
            self.grid_layout.addWidget(button, row, col)
            col += 1
            if col == 2:
                col = 0
                row += 1

        self.setLayout(self.grid_layout)
    #레이아웃 초기화 함수
    def clear_layout(self):
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()
    #마지막 상품을 띄어줄때의 테이블 초기화 함수
    def clear_table(self):
        if self.table:
            self.table.setRowCount(0)
    #DB_Code의 find_Check_Dialog 함수를 이용해서 제품명,가격,위치 불러오기
    def show_sort_categories(self, category):
        self.clear_layout()
        self.clear_table()
        conn = dbconnect(self.database)
        products = find_Check_Dialog(conn,category)

        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["품목", "가격", "위치"])
        self.grid_layout.addWidget(self.table)

        self.table.setRowCount(len(products))  # Set the row count

        for row, product in enumerate(products):
            for col, value in enumerate(product):
                self.table.setItem(row, col, QTableWidgetItem(value))

    #데이터 베이스 저장 후 서브 카테고리를 선택하면 다음 창으로 이동
    def category_clicked(self, category):
        self.clear_layout()
        
        sub_categories = []
        if category == "음식":
            self.database = "음식"
            sub_categories = ["육류", "해산물", "스낵류", "야채"]
        elif category == "가전":
            self.database = "가전"
            sub_categories = ["컴퓨터", "게이밍", "휴대폰", "TV"]
        elif category == "의류":
            self.database = "의류"
            sub_categories = ["상의", "하의", "신발", "쥬얼리"]
        elif category == "생필품":
            self.database = "생필품"
            sub_categories = ["영양제", "욕실용품", "위생용품", "화장지"]
        
        row, col = 0, 0
        for sub_category in sub_categories:
            button = QPushButton(sub_category, self)
            button.clicked.connect(lambda _, sub=sub_category: self.show_sort_categories(sub))
            button.setFixedSize(QSize(150, 150))
            self.grid_layout.addWidget(button, row, col)
            col += 1
            if col == 2:
                col = 0
                row += 1

