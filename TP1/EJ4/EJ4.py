from NodoGenerico import NodoGenerico
import math
import matplotlib.pyplot as plt
import numpy
import time
import random

def armar_espacio(num_filas, num_columnas):
    filas_mat = 5*num_filas+1
    columnas_mat = 3*num_columnas+1
    mat = {}
    cont1 = 2
    cont2 = 1
    for j in range(columnas_mat):
        for i in range(filas_mat):
            if j%3 and j!=0 and i%5 and i!=0:
                    if (j-1)%3 and not j-1==0:
                        mat[(i, j)] = cont1
                        cont1 += 2
                    if (j+1)%3:
                        mat[(i, j)] = cont2
                        cont2+=2
            else:
                mat[(i, j)] = "Pasillo"
    mat[(int(filas_mat/2), j)] = "Carga"
    mat["Filas"] = filas_mat
    mat["Columnas"] = columnas_mat
    mat["Val_max"] = (num_columnas*num_filas*8)
    return mat


class NodoParticular(NodoGenerico):
    def __init__(self, valor, padre, matriz, inicio=0, objetivo=0):
        super().__init__(valor, padre, inicio, objetivo)
        self.matriz = matriz
        self.costo = 0
        self.dist = self.getDist()

    def getDist(self):
        if self.padre:
            self.costo = self.padre.costo+0.7
        heur = math.sqrt((self.objetivo[1]-self.valor[1])**2 + (self.objetivo[0]-self.valor[0])**2)
        heur = abs(self.objetivo[1]-self.valor[1]) + abs(self.objetivo[0]-self.valor[0])
        #dist = heur + self.costo
        dist = heur
        return dist

    def crearHijos(self):
        valor = []
        if self.matriz[self.valor] == "Pasillo" or self.matriz[self.valor] == "Carga":
            if self.valor[0] != 0:
                valor = ((self.valor[0]-1), self.valor[1])
                if self.matriz[valor] == "Pasillo":
                    hijo = NodoParticular(valor, self, self.matriz)
                    self.hijos.append(hijo)
            if self.valor[1] != 0:
                valor = (self.valor[0], (self.valor[1]-1))
                hijo = NodoParticular(valor, self, self.matriz)
                self.hijos.append(hijo)
            if self.valor[0] < self.matriz["Filas"]-1:
                valor = ((self.valor[0] + 1), self.valor[1])
                if self.matriz[valor] == "Pasillo":
                    hijo = NodoParticular(valor, self, self.matriz)
                    self.hijos.append(hijo)
            if self.valor[1] < (self.matriz["Columnas"] - 1):
                valor = (self.valor[0], (self.valor[1]+1))
                hijo = NodoParticular(valor, self, self.matriz)
                self.hijos.append(hijo)
        else:
            if self.matriz[self.valor] % 2 == 0:
                valor = (self.valor[0], (self.valor[1] + 1))
                hijo = NodoParticular(valor, self, self.matriz)
                self.hijos.append(hijo)
            else:
                valor = (self.valor[0], self.valor[1] - 1)
                hijo = NodoParticular(valor, self, self.matriz)
                self.hijos.append(hijo)


class Temple:
    def __init__(self,Temp,rate,inicio,objetivo,layout):
        list1 = list(layout.keys())
        list2 = list(layout.values())
        self.inicio = list1[list2.index(inicio)]
        self.objetivo = list1[list2.index(objetivo)]
        self.temp_init = Temp
        del list1
        del list2
        self.layout = layout
        self.rate = rate
        self.camino = []
        self.temp_act=self.temp_init

    def solver(self):
        nodo_actual = NodoParticular(self.inicio, 0, self.layout, self.inicio, self.objetivo)
        cont=0
        while(self.temp_act>0):
            if nodo_actual.valor==nodo_actual.objetivo:
                break
            if  not nodo_actual.hijos:
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
        if self.objetivo not in nodo_actual.camino:
            print("No se logró generar un camino")
            return [self.camino,10000]
        else:
            self.camino=nodo_actual.camino
        return [self.camino,nodo_actual.costo]

    def temple(self, cont):
        #self.temp_act=self.temp_init*math.exp(-cont/10000)
        self.temp_act=self.temp_init-self.rate*cont

def main():
    start_time= time.time()
    matriz = armar_espacio(2, 2)
    mat=numpy.zeros((matriz["Filas"],matriz["Columnas"]))
    valor_inicio = 1
    valor_objetivo = matriz["Val_max"]
    if (matriz["Val_max"] >= valor_inicio > 0):
        if matriz["Val_max"] >= valor_objetivo > 0:
            a = Temple(0.5,0.00001,valor_inicio,valor_objetivo,matriz)
            camino= a.solver()
            if camino[0]:
                for i in camino[0]:
                    print(i)
                print("Costo: ", round(camino[1]/0.7))
                for indice in matriz:
                    if matriz[indice]!="Pasillo" and indice!="Filas" and indice!="Columnas" and indice!="Val_max":
                        mat[indice[0]][indice[1]]=5
                mat[camino[0][0][0]][camino[0][0][1]]=10
                mat[camino[0][len(camino[0])-1][0]][camino[0][len(camino[0])-1][1]]=10
                for camino in camino[0][1:len(camino[0])-1]:
                    mat[camino[0]][camino[1]]=8
                plt.imshow(mat)
                print("--- %s seconds ---" % (time.time() - start_time))
                plt.show()
        else:
            print("Estas por fuera del espacio de trabajo")
    else:
        print("Estas por fuera del espacio de trabajo")
if __name__=="__main__":
    main()