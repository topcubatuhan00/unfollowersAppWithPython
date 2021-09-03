from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys, app


class MainForm(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Unfollowers')
        self.setGeometry(450, 250, 960, 540)

        self.setWindowIcon(QIcon('./logo.png'))
        self.setStyleSheet('background-color: #edf6f9')

        self.initUI()

    def initUI(self):

        self.labelUsername = QtWidgets.QLabel(self)
        self.labelUsername.setStyleSheet("background-color:#83c5be; font-size:20px; color:#073b4c;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.labelUsername.setAlignment(QtCore.Qt.AlignCenter)
        self.labelUsername.setText("Username =>")
        self.labelUsername.resize(250,75)
        self.labelUsername.move(200,95)

        self.textUsername = QtWidgets.QLineEdit(self)
        self.textUsername.setStyleSheet("background-color:#006d77; font-size:20px; color:#edf6f9; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.textUsername.setAlignment(QtCore.Qt.AlignCenter)
        self.textUsername.resize(250,75)
        self.textUsername.move(510,95)

        self.labelPass = QtWidgets.QLabel(self)
        self.labelPass.setStyleSheet("background-color:#83c5be; font-size:20px; color:#073b4c;border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.labelPass.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPass.setText("Password =>")
        self.labelPass.resize(250,75)
        self.labelPass.move(200,220)

        self.textPass = QtWidgets.QLineEdit(self)
        self.textPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textPass.setStyleSheet("background-color:#006d77; font-size:20px; color:#edf6f9; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px")
        self.textPass.setAlignment(QtCore.Qt.AlignCenter)
        self.textPass.resize(250,75)
        self.textPass.move(510,220)

        self.buttonLogin = QPushButton("Login", self)
        self.buttonLogin.setStyleSheet('background-color:#edf6f9; color:#006d77; font-size:18px;border: 1px solid #e29578; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px')
        self.buttonLogin.resize(100,50)
        self.buttonLogin.move(430,350)
        self.buttonLogin.clicked.connect(self.login)

    def login(self):

        global globalUnfollowersList
        globalUnfollowersList = []

        self.message = QMessageBox()
        self.message.setIcon(QMessageBox.Information)
        self.message.setText("Loading Please Wait Dont Close Any Window!!")
        self.message.setWindowTitle("Loading!")

        self.message.exec_()

        self.username = self.textUsername.text()
        self.password = self.textPass.text()

        self.textUsername.setText(" ")
        self.textPass.setText(" ")
        
        app.login(self.username, self.password)

        globalUnfollowersList = app.unf()

        self.detail = DetailPage()
        self.detail.show()
        self.hide()
    
class DetailPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Details')
        self.setGeometry(450, 250, 960, 540)
        self.setWindowIcon(QIcon('./logo.png'))
        self.setStyleSheet('background-color: #edf6f9')

        self.initUI()


    def initUI(self):
        

        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        self.text1 = QtWidgets.QLabel(self)
        self.text1.setStyleSheet("font-size:20px; border-top-left-radius :10px; border-top-right-radius : 10px; border-bottom-left-radius : 10px; border-bottom-right-radius : 10px; color:#03045e; border-bottom: 1px solid #03045e;")
        self.text1.setAlignment(QtCore.Qt.AlignCenter)
        self.text1.setText("Account")
        self.text1.resize(200,50)
        self.text1.move(370,0)


        self.show()

    def createTable(self):

        self.tableWidget = QTableWidget()
        self.tableWidget.setStyleSheet("""
                font-size:24px; 
                color:#03045e;
                margin-left: 250px;
                margin-top: 75px;
                border: none;
            """)
        header = self.tableWidget.horizontalHeader()
        
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.move(500, 50)
        self.tableWidget.setRowCount(len(globalUnfollowersList))
        self.tableWidget.setColumnCount(1)
        x = 0
        y = 0
        for account in globalUnfollowersList:
            self.tableWidget.setItem(x, y, QTableWidgetItem("                "+account+"    "))
            x+=1

        self.tableWidget.doubleClicked.connect(self.doubleClickEvent)
    
    def doubleClickEvent(self):
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.text())

def run():
    application = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(application.exec_())

run()