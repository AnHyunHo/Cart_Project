from Chose_Category.EmployeeCallDialog import *
from Chose_Category.Check_out_Dialog import *
from Chose_Category.Baguni_Dialog import *
from Chose_Category.Checking_Dialog import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 407)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hochul = QtWidgets.QPushButton(self.centralwidget)
        self.hochul.setGeometry(QtCore.QRect(10, 10, 181, 191))
        self.hochul.setObjectName("hochul")
        self.checking = QtWidgets.QPushButton(self.centralwidget)
        self.checking.setGeometry(QtCore.QRect(200, 210, 191, 211))
        self.checking.setObjectName("checking")
        # self.check_out = QtWidgets.QPushButton(self.centralwidget)
        # self.check_out.setGeometry(QtCore.QRect(200, 10, 191, 191))
        # self.check_out.setObjectName("check_out")
        self.host = QtWidgets.QPushButton(self.centralwidget)
        self.host.setGeometry(QtCore.QRect(10, 210, 181, 211))
        self.host.setObjectName("host")
        self.baguni = QtWidgets.QPushButton(self.centralwidget)
        self.baguni.setGeometry(QtCore.QRect(400, 10, 391, 411))
        self.baguni.setObjectName("baguni")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 585, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.hochul.clicked.connect(self.openEmployeeCallDialog)
        # self.check_out.clicked.connect(self.opencheck_out_Dialog)
        self.baguni.clicked.connect(self.openbaguni_Dialog)
        self.checking.clicked.connect(self.openchecking_Dialog)
        self.retranslateUi(MainWindow)






    def openEmployeeCallDialog(self):
        self.employee_call_dialog = EmployeeCallDialog()
        self.employee_call_dialog.exec_()

    def opencheck_out_Dialog(self):
        self.check_out_Dialog = Check_out_Dialog()
        self.check_out_Dialog.exec_()

    def openbaguni_Dialog(self):
        self.baguni_Dialog = Baguni_Dialog()
        self.baguni_Dialog.exec_()

    def openchecking_Dialog(self):
        self.checking_DIalog = Checking_Dialog()
        self.checking_DIalog.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hochul.setText(_translate("MainWindow", "직원 호출"))
        self.checking.setText(_translate("MainWindow", "상품확인"))
        # self.check_out.setText(_translate("MainWindow", "결제"))
        self.host.setText(_translate("MainWindow", "관리자"))
        self.baguni.setText(_translate("MainWindow", "장바구니"))
