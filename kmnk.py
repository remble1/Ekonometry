from PyQt6 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
import math
import statistics
from itertools import product
from pandas.core.arrays.sparse import dtype
from PyQt6.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt6.QtGui import QIcon

def kmnk():
    file_name = 'D:/Workspace/Ekonometry/Ekonometry/dane.xlsx'
    sheet = 'date'  # nazwa arkusza z tabelą

    data1 = pd.read_excel(file_name, sheet_name=sheet, header=None,
                          engine='openpyxl')  # pobrane dane z arkusza przy czym 1 wiersz to nazwy,
    # ponieważ z funkcją read_excel są trudne do pozyskania
    data2 = pd.read_excel(file_name, sheet_name=sheet, engine='openpyxl')  # faktyczne dane

    y = data1.iloc[3][0]  # nazwa zmiennej objasnianej jej pozycja w tabeli

    var_number = len(data1.loc[0])  # liczba wszystkich zmiennych Y X1 X2 X3 X4

    print(data1.iloc[0:12, 0: 1])
    dataKmnk = data1.iloc[:, :-1]
    products_list = dataKmnk.values.tolist()
    print(products_list)
    a = np.array(products_list)
    print(a)
    b = a.transpose()
    print(b)

a = 'derddddddddddddddddddrffffe'
print((a[:8]))
