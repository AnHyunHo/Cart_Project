import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from DB_Code import *
from Sort_Function import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QDialog
from PyQt5.QtCore import QSize

class Check_out_Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None , save_data = None):
        super().__init__(parent)
        self.save_data = save_data
        self.setWindowTitle("결제 창")
        self.setGeometry(100, 100, 300, 150)
        self.message_label = QtWidgets.QLabel("카드를 삽입해 주세요...", self)
        self.message_label.setGeometry(75, 20, 200, 30)
        self.ok_button=QtWidgets.QPushButton("확인",self)
        self.ok_button.setGeometry(100,70,100,30)
        self.ok_button.clicked.connect(self.handle_ok_button)

        self.return_button = QtWidgets.QPushButton("돌아가기", self)
        self.return_button.setGeometry(100, 110, 100, 30)
        self.return_button.clicked.connect(self.close)
   
       
    
    def handle_ok_button(self):
    # 품목별 재고(stock) 감소 및 장바구니 초기화
        for item_name, item_data in self.parent().cart.items():
            quantity = item_data['quantity']
            save_data = self.save_data
            # 데이터베이스에서 해당 품목의 stock 조회
            stock = get_stock_from_database(save_data,item_name)
            
            # 수량만큼 재고(stock) 감소 후 업데이트
            new_stock = stock - quantity
            print(new_stock)
            update_stock_in_database(item_name, new_stock,save_data)
        
        # 장바구니 리스트 초기화
        self.parent().cart = {}
        self.parent().total_price = 0
        self.parent().update_cart_table()
        self.parent().update_total_display()
        
        QMessageBox.information(self, "결제 완료", "결제가 완료되었습니다.")
        # 결제 창 닫기
        self.parent().hide()
        self.accept()

def get_stock_from_database(save_data,item_name):
    i = 0
    while i < len(save_data):
        if item_name == save_data[i][2]:
            database = save_data[i][0]
            table = save_data[i][1]
        i += 1
    

    conn = dbconnect(database)
    result = search_data(conn, table, "stock", item_name)
    conn.close()

    if result:
        return result[0][0]
    return 0  # 만약 해당 품목이 데이터베이스에 없으면 재고는 0으로 간주

# 데이터베이스에서 품목의 재고(stock) 업데이트
def update_stock_in_database(item_name, new_stock,save_data):
    i = 0
    while i < len(save_data):
        if item_name == save_data[i][2]:
            database = save_data[i][0]
            table = save_data[i][1]
        i += 1

    conn = dbconnect(database)
    cur = conn.cursor()

    sql = f'UPDATE {table} SET stock = {new_stock} WHERE name = \'{item_name}\''
    cur.execute(sql)
    conn.commit()

    conn.close()







