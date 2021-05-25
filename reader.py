import numpy as np
import pandas as pd

sheets = pd.read_excel('dane.xlsx') # czytanie z excela
# sheets to dataFrame

print(type(sheets))
zmiennaY = sheets['Y'].tolist()
zmiennaX1 = sheets['X1'].tolist()
zmiennaX2 = sheets['X2'].tolist()
zmiennaX3 = sheets['X3'].tolist()
zmiennaX4 = sheets['X4'].tolist()


dataDict = sheets.to_dict()
#yColumn = dict[0]
print(f"Lista zmiennej Y:{zmiennaY}\nLista zmiennej X1:{zmiennaX1}\nLista zmiennej X2:{zmiennaX2}\nLista zmiennej X3: {zmiennaX3}\nLista zmiennej X4: {zmiennaX4}\n")




"""df = pd.DataFrame(products, columns= ['Product', 'Price'])

products_list = [df.columns.values.tolist()] + df.values.tolist()
f = '{:<8}|{:<15}' # formatting

for i in products_list:
    print(f.format(*i))"""

