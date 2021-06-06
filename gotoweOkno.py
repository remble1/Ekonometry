from PyQt6 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
import math
import statistics
from itertools import product
from pandas.core.arrays.sparse import dtype
from PyQt6.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt6.QtGui import QIcon
import subprocess


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(728, 496)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 30, 151, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 110, 301, 311))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 30, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 110, 301, 350))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 22))
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
        self.pushButton.setText(_translate("MainWindow", "Załaduj plik"))
        self.label.setText(_translate("MainWindow", "Witaj w programie!\n"
        "\n"
        "1. Proszę przygotuj sobie plik exel o rozszerzeniu\n"
        " .xlsx tak aby pierwszy wiersz miał tytuły Y, X1, X2,\n"
        " X3 i X4. a poniżej w kolumnach były wartości. \n"
        "\n"
        "2. Przyciśnij przycisk \"Załaduj plik\" i wybierz plik\n"
        " w którym są dane. \n"
        "\n"
        "3. Przyciśnij przycisk \"Podaj wyniki\" aby zobaczyć\n"
        " przebieg i wyniki. \n"
        "\n"
        "\n"
        "\n"
        "\n"
        "\n"
        "\n"
        " Autor programu: Paweł Sadkowski "))


        self.pushButton_2.setText(_translate("MainWindow", "Podaj wyniki"))
        self.label_2.setText(_translate("MainWindow", "Wyniki obliczeń pojawią się po rozpoczęciu liczenia."))
        self.pushButton.clicked.connect(self.open_dialog_box)
        self.pushButton_2.clicked.connect(self.hellwig)

        #self.pushButton_2.clicked.connect(self.kmnk)
        self.file_name = ""
        self.tekst = []

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        self.file_name = filename[0]
        print(self.file_name)  # exel file path

    def start_count(self):
        self.label_2.setText(self.file_name)
        print("start count")
        print(self.file_name)

    def update(self):
        self.label.adjustSize()

    def hellwig(self):

        # Deklaracja używanych danych
        self.tekst = []
        #self.file_name = 'D:/Workspace/Ekonometry/Ekonometry/dane.xlsx'  # nazwa dokumentu Excel o rozszerzeniu xslx
        print(self.file_name)
        file_name = self.file_name
        sheet = 'date'  # nazwa arkusza z tabelą

        data1 = pd.read_excel(file_name, sheet_name=sheet, header=None,
                              engine='openpyxl')  # pobrane dane z arkusza przy czym 1 wiersz to nazwy,
        # ponieważ z funkcją read_excel są trudne do pozyskania
        data2 = pd.read_excel(file_name, sheet_name=sheet, engine='openpyxl')  # faktyczne dane

        y = data1.iloc[0][0]  # nazwa zmiennej objasnianej jej pozycja w tabeli

        var_number = len(data1.loc[0])  # liczba wszystkich zmiennych Y X1 X2 X3 X4
        #print(f"Ilość zmiennych wraz z Y to {var_number - 1}\n")
        variables = []  # wszystkie zmienne objasniajace spelnaijace Vj > 10%
        var_cor = []  # wszystkie współczynniki korelacji miedzy zmiennymi objaśniajacymi a objaśnianą
        H = []  # integralne wskaźniki integralności informacyjnej
        var_win = []  # najlepsze zmienne objaśniające

        # ETAP 1 - wspolczynnik zmiennosci Vj > 10%
        i = 0  # TU POWINNO BYC 0


        for c in range(1, var_number):  # dla każdej kolumny poza kolumną 1 ze zmienna objaśnianą
            xi = data1.loc[:, i]  # wszystkie wartosci liczbowe z kolumny
            xi = xi.loc[
                 1:,
                 ]  # nie branie pod uwagę 1 wiersza z wartościami nieliczbowymi (nazwy kolumn) nazwa kolumny liczbowej
            mean = statistics.mean(xi)  # średnia zmiennej

            if c == 1:
                a1 = f"Srednia zmiennej Y wynosi {mean}\n"
                self.tekst.append(a1)
                sd = statistics.stdev(xi)  # odchylenie standardowe zmiennej
                a2 = f"Odchylenie standardowe Y wynosi {sd}\n"
                self.tekst.append(a2)
                vj = sd / mean  # współczynnik zmienności
                a3 = f"współczynnik zmienności Y wynosi {vj}\n"
                self.tekst.append(a3)
                self.tekst.append("\n")
            else:
                a4 = f"Srednia zmiennej X{c-1} wynosi {mean}\n"
                self.tekst.append(a4)
                sd = statistics.stdev(xi)  # odchylenie standardowe zmiennej
                a5 = f"Odchylenie standardowe X{c-1} wynosi {sd}\n"
                self.tekst.append(a5)
                vj = sd / mean  # współczynnik zmienności
                a6 = f"współczynnik zmienności X{c-1} wynosi {vj}\n"
                self.tekst.append(a6)
                self.tekst.append("\n")

            atr = data1.iloc[0][i]  # atrybut zmiennej, która spełnia warunek Vj > 10%
            if vj > 0.1:
                variables.append(atr)  # dodawania atrybutów poprawnych zmiennych do listy
            i += 1


        self.label_2.setText(' '.join(self.tekst))
        self.update()

        #print(f"zmienne nadające się mające tą zmienność +0.1 {variables}")
        # print("dupa", "\n")

        # ETAP 2 - macierz binarna reprezentująca możliwe kombinacje
        m = len(variables) - 1  # m jest liczbą zmiennych objaśniajacych, kolumny w macierzy binarnej
        S = 2 ** m - 1  # liczba kombinacji przepuszczonych zmiennych objaśniających, liczba wierszy macierzy binarnej
        binary_matrix = [i for i in product(range(2),
                                            repeat=m)]  # dwie linijki kodu generujące dowolną macierz z wszystkimi kombinacjami 0-1
        binary_matrix = np.array(binary_matrix)
        binary_matrix = np.delete(binary_matrix, 0, axis=0)  # usunięcie 1 wiersza z wygenerowanymi 0
        print(f"{binary_matrix} \n")

        dataSmall = data2.iloc[:, :-1]

        # ETAP 3 - macierz korelacji reprezentująca bezwzgledne korelacje między wszystkimi zmiennymi odniesienie do |rij|
        data3 = pd.DataFrame(dataSmall)
        corr_frame = np.absolute(data3.corr())  # wartości bezwglądne współczynników korelacji wraz z opisami
        corr_matrix = corr_frame.values  # zamiana ramki na macierz
        corr_matrix = corr_matrix.round(decimals=6, out=None)

        for i in range(1, m + 1):  # przekazanie współczynników korelacji między xi a y rj - potrzebne do obliczania h
            var_cor.append(corr_matrix[0][i - 1])

        corr_matrix = np.delete(corr_matrix, 0,
                                axis=0)  # usuniecie pierwszego wiersza i  kolumny z korelacją x i y, ponieważ potem jest
        corr_matrix = np.delete(corr_matrix, 0, axis=1)  # obliczanie sumy rij
        print(f"{corr_frame} \n")
        print(f"{corr_matrix} \n")
        print("\n")
        #print(f"liczba S wynosi {S} liczba m wynosi {m}\n")
        # ETAP 4 - obliczanie indywidualnych wskaźników pojemności informacyjnej h
        final_matrix = binary_matrix

        final_matrix = final_matrix.astype('float64')
        # print(final_matrix)

        for i in range(0, S):  # liczba S wierszy macierzy bin wiec jedzie w dół jest ich 15
            for j in range(0, m):  # m czyli szerokosc jest icj 4
                if final_matrix[i][j] == 1:
                    h = np.square(var_cor[j]) / np.sum(final_matrix[i].dot(corr_matrix[j]))  # cco to sie dzieje
                    h = h.round(decimals=6, out=None)
                    final_matrix[i][j] = h

        print(f"oblicznie małego h w tle\n")

        # ETAP 5 - obliczanie integralnych wskaźników pojemnosci informacyjnej
        for i in range(0, S):  # kolejne H są dodawane do listy, potem na podstawie pozycji znajdzie się index
            s = np.sum(final_matrix[i])  # najlepszej kombinacji zmiennych objaśniających
            s = round(s, 6)  # zaokrągla wartosc S do 6 liczb po przecinku
            H.append(s)
            print(f"C{i} -- {sum(H)}")  # pusta lista WTF

        max_H = max(H)  # najwyzsze H
        idx = 0  # poszukiwany index
        while True:  # przeszukiwanie listy H w poszukiwaniu pozycji max H
            if H[idx] == max_H:
                break
            idx += 1

        # ETAP 6 - znalezienie najlepszej kombinacji i prezentacja wyników
        binary_matrix = binary_matrix.astype('float64')
        for i in range(0, m):  # wypełnianie listy nazwami zmiennych z najlepszej kombinacji
            if binary_matrix[idx][i] == 1:
                var_win.append(variables[i])

        print(f"\nOptymalnym zbiorem zmiennych objaśniających jest kombinacja C{idx}")
        for i in range(len(var_win)):
            print(var_win[i])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
