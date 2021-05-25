import numpy as np
import pandas as pd
try:
    sheets = pd.read_excel('dane.xlsx') # czytanie z excela
    # sheets to dataFrame
except:
    print("Brak pliku o odpowiedniej nazwie")
    print("Dolocz do folderu plik o formacie .xlsx z 5 kolumnami zmiennych Y, X1, X2, X3 i X4")

#print(type(sheets))
zmiennaY = sheets['Y'].tolist()
zmiennaX1 = sheets['X1'].tolist()
zmiennaX2 = sheets['X2'].tolist()
zmiennaX3 = sheets['X3'].tolist()
zmiennaX4 = sheets['X4'].tolist()

"""if len(zmiennaY) or len(zmiennaX1) or len(zmiennaX2) or len(zmiennaX3) or len(zmiennaX4) >= 13:
    print("Zmienne w pliku .xlsx maja zla dlugosc \n Kazda kolumna powinna miec 11 wartosci")

print(len(zmiennaX4),len(zmiennaX3),len(zmiennaX2),len(zmiennaX1),len(zmiennaY))"""

sumY = sum(zmiennaY)
sumX1 = sum(zmiennaX1)
sumX2 = sum(zmiennaX2)
sumX3 = sum(zmiennaX3)
sumX4 = sum(zmiennaX4)

def r0():
    arr = np.array([zmiennaX1, zmiennaX2, zmiennaX3, zmiennaX4])
    np.mean(arr, axis=0)

# dataDict = sheets.to_dict() zamiana dataFrame na dict

print(f"Lista zmiennej Y:{zmiennaY}\nLista zmiennej X1:{zmiennaX1}\nLista zmiennej X2:{zmiennaX2}\nLista zmiennej X3: {zmiennaX3}\nLista zmiennej X4: {zmiennaX4}\n")

print(sumY)


"""df = pd.DataFrame(products, columns= ['Product', 'Price'])

products_list = [df.columns.values.tolist()] + df.values.tolist()
f = '{:<8}|{:<15}' # formatting

for i in products_list:
    print(f.format(*i))"""

