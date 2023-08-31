import sys,pickle,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DB_Code import *
from Chose_Category.Check_out_Dialog import *
#장바구니를 선택하였을때 클래스
class Baguni_Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("장바구니 리스트")
        self.setGeometry(1000, 1000, 630, 600)
        self.save_data = []
        self.cart = {}
        self.total_price = 0
        self.init_ui()
        self.return_button = QtWidgets.QPushButton("돌아가기", self)
        self.return_button.setGeometry(100, 500, 100, 30)
        self.return_button.clicked.connect(self.close)
        self.item_list2 = ""
        self.load_cart_data()  #바구니 창을 열떄 load_cart_data()를 통해서 cart_data_pkl파일에 데이터를 참조하여 화면에 출력함
        self.check_save_num=0
        
        self.move_to_center()
    
    def move_to_center(self):
        screen_geometry = QtWidgets.QApplication.desktop().screenGeometry()
        dialog_geometry = self.frameGeometry()
        x = (screen_geometry.width() - dialog_geometry.width()) // 2
        y = (screen_geometry.height() - dialog_geometry.height()) // 2
        self.move(x, y)

    
        

        
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, "장바구니 저장", "장바구니 내용을 저장하시겠습니까?", 
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            check_save_num=0
            self.save_cart_data(check_save_num)  # 장바구니 내용 저장
        else:
            self.cart = {}
            self.total_price = 0
            check_save_num=1
            self.save_cart_data(check_save_num)  # 데이터 초기화 후 저장
            self.hide()  # 창을 숨김
            #  # "아니오"를 선택한 경우 cart_data.pkl 파일 삭제
            # try:
            #     os.remove('cart_data.pkl')
            # except FileNotFoundError:
            #     pass
        
            # self.hide()  # 창을 숨김
            # event.ignore()  # 창을 닫는 이벤트를 무시
        event.accept()  # 창 닫기 이벤트 수행
    def save_cart_data(self,check_save_num):   #위에 closeEvent에서 닫기버튼->yes,no로 나뉘는데
        cart_data = {                          #yes를 누르면 지금 품목과 price를  cart_data에 담아서 pkl파일에 저장
            'cart': self.cart,                 #no를 누르면 품목과 price를 모두 초기화 한 상태에서 cart_data에 담아 pkl파일 저장
            'total_price': self.total_price
        }
        with open('cart_data.pkl', 'wb') as f:
            pickle.dump(cart_data, f)
            if(check_save_num==0):
                 QMessageBox.information(self, "저장 완료", "장바구니 내용이 저장되었습니다.")
            else:
                QMessageBox.information(self, "저장 완료", "장바구니 내용이 초기화되었습니다.")


    def load_cart_data(self):       #바구창 열 때 cart_data.pkl를 확인해서 내용이 있으면 불러오고 , 없으면 초기화상태에서 시작.
        try:
            with open('cart_data.pkl', 'rb') as f:
                cart_data = pickle.load(f)
                if 'cart' in cart_data:
                    self.cart = cart_data['cart']
                if 'total_price' in cart_data:
                    self.total_price = cart_data['total_price']
                self.update_cart_table()
                self.update_total_display()
        except FileNotFoundError:
            pass


    def init_ui(self):
        self.cart_table = QtWidgets.QTableWidget(self)
        self.cart_table.setGeometry(20, 20, 760, 440)

        self.cart_table.setColumnCount(4)
        self.cart_table.setHorizontalHeaderLabels(["품목", "가격", "수량", "합계"])

        self.total_label = QtWidgets.QLabel("총 가격:", self)
        self.total_label.setGeometry(20, 470, 100, 30) 

        self.total_display = QtWidgets.QLabel("0원", self)
        self.total_display.setGeometry(120, 470, 100, 30) 

        self.barcode_label = QLabel("바코드 입력:", self)
        self.barcode_input = QLineEdit(self)

        self.payment_button = QPushButton("결제", self)
        self.payment_button.setGeometry(750, 470, 30, 30)
        self.payment_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.payment_button.clicked.connect(self.open_check_out_dialog)  # 결제 버튼 클릭 시에 결제 창 열기 연결

        self.close_button = QPushButton("닫기", self)
        self.close_button.setGeometry(750, 470, 30, 30)
        self.close_button.clicked.connect(self.close)  # 닫기 버튼 클릭 이벤트
        self.close_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.barcode_label)
        self.layout.addWidget(self.barcode_input)
        self.layout.addWidget(self.cart_table)
        self.layout.addWidget(self.total_label)
        self.layout.addWidget(self.total_display)
        self.layout.addWidget(self.payment_button) 
        self.layout.addWidget(self.close_button)  # 닫기 버튼 추가
       
        self.setLayout(self.layout)
        self.show()
        self.barcode_input.returnPressed.connect(self.add_to_cart)
    #결제창 열기
    def open_check_out_dialog(self):
        self.check_out_dialog = Check_out_Dialog(self,self.save_data)
        self.check_out_dialog.exec_()

    def update_total_display(self):
        self.total_display.setText(f"{self.total_price}원")

    def add_to_cart(self):
        barcode = self.barcode_input.text()
        
        if len(barcode) != 6:
            QMessageBox.warning(self, "오류", "올바른 바코드 6자리를 입력해주세요.")
            self.barcode_input.clear()
            return
        database, table, name = database_sort(barcode)
        if database is None:
            QMessageBox.warning(self, "오류", "일치하는 품목이 없습니다.")
            self.barcode_input.clear()
            return
        else :
            self.save_data.append((database, table, name))

        conns = dbconnect(database)
        item_price = search_data(conns, table, 'price', name)[0][0]

        self.item_list2 = name
        if item_price is not None:
            if self.item_list2 in self.cart:
                self.cart[self.item_list2]['quantity'] += 1
            else:
                self.cart[self.item_list2] = {'quantity': 1, 'price': item_price}

            self.total_price += item_price
            self.update_cart_table()
            self.update_total_display()
            self.barcode_input.clear()
        else:
            QMessageBox.warning(self, "오류", "일치하는 품목이 없습니다.")
            self.barcode_input.clear()
            return 
            
    
            
    def update_cart_table(self):
        self.cart_table.setRowCount(len(self.cart))
        # 상품 테이블 추가
        self.cart_table.setColumnCount(6)
        self.cart_table.setHorizontalHeaderLabels(["품목", "가격", "수량", "합계", "상품 추가", "상품 삭제"]) 

        row = 0
        for item_name, item_data in self.cart.items():
            quantity = item_data['quantity']
            price = item_data['price']
            total = quantity * price

            self.cart_table.setItem(row, 0, QtWidgets.QTableWidgetItem(item_name))
            self.cart_table.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{price}원"))
            self.cart_table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(quantity)))
            self.cart_table.setItem(row, 3, QtWidgets.QTableWidgetItem(f"{total}원"))

            #추가 버튼
            add_button = QtWidgets.QPushButton("+", self)
            add_button.clicked.connect(lambda _, r=row: self.change_quantity(r, 1))
            self.cart_table.setCellWidget(row, 4, add_button)  # 열 증가

            #삭제 버튼
            delete_button = QtWidgets.QPushButton("-", self)
            delete_button.clicked.connect(lambda _, r=row: self.change_quantity(r, -1))
            self.cart_table.setCellWidget(row, 5, delete_button)  # 열 증가

            row += 1

    def change_quantity(self, row, change):
        item_name = self.cart_table.item(row, 0).text()
        item_data = self.cart[item_name]
        item_price = item_data['price']
        current_quantity = item_data['quantity']
        #제품이 음수일때
        new_quantity = current_quantity + change
        if new_quantity < 0:
            new_quantity = 0
        # 수량이 0일때
        if new_quantity == 0:
            self.total_price -= item_price * current_quantity
            del self.cart[item_name]
        else:
            #최종 출력
            self.total_price = self.total_price - (item_price * current_quantity) + (item_price * new_quantity)
        
            self.cart[item_name]['quantity'] = new_quantity
    
        self.update_cart_table()
        self.update_total_display()