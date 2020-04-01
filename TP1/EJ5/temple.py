#Imports standart library
import math
import random
from NodoTemple import NodoTemple


class Temple:
    def __init__(self,Temp,rate,inicio,layout):
        self.inicio = inicio
        self.temp_init = Temp
        self.layout = layout
        self.rate = rate
        self.temp_act=0
        self.costos = []

    def solver(self):
        nodo_actual = NodoTemple(self.inicio, 0, self.inicio, self.layout)
        self.temp_act = self.temp_init
        cont=0
        cont2=0
        cont3=0
        self.costos.append(nodo_actual.cost)
        while(self.temp_act>0):
            if  not nodo_actual.hijos:
                nodo_actual.crearHijos()
            self.costos.append(nodo_actual.cost)
            nodo_siguiente=random.choice(nodo_actual.hijos)
            E = nodo_actual.cost-nodo_siguiente.cost
            if E>0:
                nodo_actual=nodo_siguiente
            else:
                cont2 += 1
                if math.exp(E/self.temp_act)>=random.random():
                    nodo_actual = nodo_siguiente
                    cont3+=1
            cont+=1
            self.temple(cont)
        acc_percent=cont3/cont2*100
        return [nodo_actual.valor,nodo_actual.cost,acc_percent,self.costos]

    def temple(self, cont):
        #self.temp_act=self.temp_init*math.exp(-cont/self.rate)
        self.temp_act=self.temp_init-self.temp_init/self.rate*cont