from PyQt6 import QtCore, QtGui, QtWidgets

from PyQt6.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt6.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(253, 323)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 40, 151, 41)) # zaladuj plik
        self.pushButton.setObjectName("pushButton")


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget) # podaj wynik
        self.pushButton_2.setGeometry(QtCore.QRect(50, 110, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 253, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ekonometria"))
        self.pushButton.setText(_translate("MainWindow", "Zaladuj plik"))
        self.pushButton_2.setText(_translate("MainWindow", "Podaj wyniki"))
        self.pushButton.clicked.connect(self.open_dialog_box)
        self.pushButton_2.clicked.connect(self.start_count)

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        path_exel = filename[0]
        print(path_exel)  # exel file path

    def start_count(self):
        print("start count")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
