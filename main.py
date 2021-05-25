from sklearn import datasets
import hellwing as H
import pandas as pd
import numpy as np

if __name__ == "__main__":
    sheets = pd.read_excel('dane.xlsx')
    X = sheets['X1'].tolist()
    Y = sheets['Y'].tolist()
#    feature_names = iris_data.feature_names
    Combinations = []

    new_X = []
    for i in range(len(X[0])):
        out = []
        for j in range(len(X)):
            out.append(X[j][i])
        new_X.append(out)

    new_X = np.array(new_X)
    X = new_X

    Hel = H.Hellwig(X, Y)


    print("Macierz R")
    '''
    print(Hel.R)
    print("")
    print("Macierz R0")
    print(Hel.R0)
    print("Elementy h:")
    for combination in Hel.h:
        print(combination)
    print("")
    print("Elementy H:")
    for combination in Hel.H:
        print(combination)
    print('')
    '''

    print("Variables: ", feature_names)
    print("Doing Hellwig stuff...")
    valid = []
    for element in Hel.Answer:
        valid.append(feature_names[int(element)])
    print("Valid variables: ", valid)