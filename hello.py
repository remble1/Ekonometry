from itertools import combinations

import numpy as np
import scipy as sp

# wczytac z pliku liste X z pliku CSV
class Hellwig:
    def __init__(self, X, Y):
        self.X = X # lista X
        self.Y = Y # lista Y 
        self.N = len(self.X)
        self.Combinations = self.All(self.X)
        self.R0 = self.CreateR0()
        self.R = self.CreateR()
        self.h = self.Createh()
        self.H = self.CreateH()
        self.Answer = np.array(self.Combinations[np.argmax(self.H)]) # tablica z numpy

    def __str__(self):
        return str(self.Answer) # objekt zwraca str


    def n(self, arr, n):
        if len(arr) == 1:
            #val = arr[0]
            #return np.array([[val, val]])
            pass
        return list(combinations(arr, n))

    def All(self, arr): # bierze tablice
        output = []
        N = range(len(arr))
        for n in N:
            n += 1
            tmp = self.n(N, n)
            for i in tmp:
                output.append(list(i))
        return np.array(output)

    def CreateR0(self):
        tmp = np.zeros(self.N)
        for i, x in enumerate(self.X):
            tmp[i] = sp.stats.pearsonr(self.Y, x)[0]
        return tmp


    def CreateR(self):
        self.R = np.array
        tmp = np.zeros((self.N, self.N))
        for i, x1 in enumerate(self.X):
            for j, x2 in enumerate(self.X):
                tmp[i][j] = sp.stats.pearsonr(x1, x2)[0]
        return tmp

    def Createh(self):
        tmp = self.Combinations
        output = []
        for t in tmp:
            o = []
            mianownik = 0
            for j in t:
                mianownik += np.absolute(self.R[t[0]][j])
            for j in t:
                o.append(self.R0[j]**2/mianownik)
            output.append(o)
        return np.array(output)

    def CreateH(self):
        tmp = []
        for combination in self.h:
            tmp.append(np.sum(combination))
        return np.array(tmp)


