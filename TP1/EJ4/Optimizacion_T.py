from NodoGenerico import NodoGenerico
from EJ4 import armar_espacio
from EJ4 import Temple
import math
import random
matriz = armar_espacio(2,2)


class NodoParticular(NodoGenerico):
    def __init__(self, valor, padre, inicio=0, objetivo=0):
        super().__init__(valor, padre, inicio, objetivo)
        a = Temple(self.valor,0.000000005,1,matriz["Val_max"],matriz)
        self.dist = a.solver()[1]

    def crearHijos(self):
            hijo = NodoParticular(self.valor+0.02, self)
            self.hijos.append(hijo)
            hijo = NodoParticular(self.valor-0.02, self)
            self.hijos.append(hijo)


class Temple2:

    def __init__(self,Temp,rate,inicio,objetivo):
        self.inicio = inicio
        self.objetivo = objetivo
        self.temp_init = Temp
        self.rate = rate
        self.camino = []
        self.temp_act=self.temp_init

    def solver(self):
        nodo_actual = NodoParticular(self.inicio, 0, self.inicio, self.objetivo)
        cont=0
        while(self.temp_act>0):
            nodo_actual.crearHijos()
            nodo_siguiente=random.choice(nodo_actual.hijos)
            E=nodo_actual.dist-nodo_siguiente.dist
            if E>0:
                nodo_actual=nodo_siguiente
            else:
                if math.exp(E/self.temp_act)>=random.random():
                    nodo_actual=nodo_siguiente
            cont+=1
            self.temple(cont)
        return [nodo_actual.valor,nodo_actual.dist]

    def temple(self, cont):
        self.temp_act=self.temp_init-self.rate*cont

valor_init=0.5
valor_objetivo=1000
b = Temple2(100,1,valor_init,valor_objetivo)
resultado = b.solver()
print(resultado)