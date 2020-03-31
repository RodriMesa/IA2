from NodoGenerico import NodoGenerico
from Astar import Asolver
import random

class NodoTemple(NodoGenerico):
    def __init__(self,valor,padre,inicio=0,layout=0):
        super().__init__(valor,padre,inicio)
        if not self.padre:
            self.layout = layout
        else:
            self.layout=self.padre.layout
        self.cost = self.getDist()

    def getDist(self):
        costo=0
        for i in range(len(self.valor)-1):
            a = Asolver(self.valor[i],self.valor[i+1],self.layout)
            costo += round(a.solver()[1]/0.7)
        return costo
    
    def crearHijos(self):
        b=random.sample(range(len(self.valor)),2)
        pos1=int(b[0])
        pos2=int(b[1])
        val = list(self.valor)
        temp = val[pos1]
        val[pos1] = val[pos2]
        val[pos2] = temp
        hijo = NodoTemple(tuple(val),self)
        self.hijos.append(hijo)