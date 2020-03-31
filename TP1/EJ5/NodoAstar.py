from NodoGenerico import NodoGenerico
import math


class NodoAstar(NodoGenerico):
    def __init__(self, valor, padre, matriz, inicio=0, objetivo=0):
        super().__init__(valor, padre, inicio, objetivo)
        self.costo_paso = 0.7
        self.matriz = matriz
        self.costo = 0
        self.dist = self.getDist()
        

    def getDist(self):
        if self.padre:
            self.costo = self.padre.costo+self.costo_paso
        heur = math.sqrt((self.objetivo[1]-self.valor[1])**2 + (self.objetivo[0]-self.valor[0])**2)
        dist = heur + self.costo
        return dist

    def crearHijos(self):
        valor = []
        if self.matriz[self.valor] == "Pasillo":
            if self.valor[0] != 0:
                valor = ((self.valor[0]-1), self.valor[1])
                if self.matriz[valor] == "Pasillo":
                    hijo = NodoAstar(valor, self, self.matriz)
                    self.hijos.append(hijo)
            if self.valor[1] != 0:
                valor = (self.valor[0], (self.valor[1]-1))
                hijo = NodoAstar(valor, self, self.matriz)
                self.hijos.append(hijo)
            if self.valor[0] < self.matriz["Filas"]-1:
                valor = ((self.valor[0] + 1), self.valor[1])
                if self.matriz[valor] == "Pasillo":
                    hijo = NodoAstar(valor, self, self.matriz)
                    self.hijos.append(hijo)
            if self.valor[1] < (self.matriz["Columnas"] - 1):
                valor = (self.valor[0], (self.valor[1]+1))
                hijo = NodoAstar(valor, self, self.matriz)
                self.hijos.append(hijo)
        else:
            if self.matriz[self.valor] % 2 == 0:
                valor = (self.valor[0], (self.valor[1] + 1))
                hijo = NodoAstar(valor, self, self.matriz)
                self.hijos.append(hijo)
            else:
                valor = (self.valor[0], self.valor[1] - 1)
                hijo = NodoAstar(valor, self, self.matriz)
                self.hijos.append(hijo)